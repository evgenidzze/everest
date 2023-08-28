from functools import wraps
from flask import request, jsonify
from jsonrpc.backend.flask import api
from market import app
from market.models import Order

app.register_blueprint(api.as_blueprint())
app.add_url_rule('/api', 'api', api.as_view(), methods=['POST'])

USER_PASSWORDS = {
    'username': 'password',
}


# Функція для перевірки авторизації
def check_auth(username, password):
    return USER_PASSWORDS.get(username) == password


# Функція-декоратор для авторизації
def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return jsonify({'message': 'Authentication required'}), 401
        return f(*args, **kwargs)

    return decorated


@api.dispatcher.add_method
@requires_auth
def get_order_status(order_num):
    order = Order.query.filter_by(id=order_num).first()
    return order.status
