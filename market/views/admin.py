from flask import session, abort
from flask_admin import AdminIndexView, expose, Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user

from market import app, celery, db
from market.models import Order, Item, User


class SecureModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin

    def not_auth(self):
        return 'you are not authorized'


class MyHomeView(AdminIndexView):
    @expose('/')
    def index(self):
        orders = Order.query.all()
        all_items = Item.query.all()
        if current_user.is_authenticated and current_user.is_admin:
            return self.render('admin/index.html', orders=orders, items=all_items)
        else:
            return abort(403)


admin = Admin(app, index_view=MyHomeView(name='Dashboard'), template_mode='bootstrap3')


class OrderViewAdmin(SecureModelView):
    form_choices = {
        'status': [
            ('COMPLETED', 'COMPLETED'),
            ('PROCESSING', 'PROCESSING'),
            ('CANCELED', 'CANCELED'),
        ]
    }

    def on_model_change(self, form, model, is_created):
        if form.data['status']:
            create_order_status_history.delay(model.id, model.status)


@celery.task
def create_order_status_history(order_id, status):
    with open('order_status_history', 'a') as file:
        file.write(f'Order: {order_id} changed status to {status}\n')


admin.add_view(SecureModelView(User, db.session))
admin.add_view(SecureModelView(Item, db.session))
admin.add_view(OrderViewAdmin(Order, db.session))
