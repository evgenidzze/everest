from flask import render_template, redirect, url_for, flash, session, jsonify
from market.handlers import handle_cart
from market import app, db
from market.models import Item, Order, OrderItems, City, Country
from market.forms import AddToCart, CheckoutForm
from flask_login import login_required


@app.route('/', methods=['POST', 'GET'])
def catalog_page():
    items = Item.query.order_by(Item.price).all()
    add_to_cart_form = AddToCart()
    return render_template('catalog.html', data=items, cart_form=add_to_cart_form)


@app.route('/add_to_cart', methods=['POST'])
@login_required
def add_to_cart():
    if 'cart' not in session:
        session['cart'] = []
    form = AddToCart()
    if form.validate_on_submit():
        session['cart'].append({'id': form.id.data, 'quantity': form.quantity.data})
        session.modified = True
    else:
        for err_msg in form.errors.values():
            flash(f"Error with adding to cart: {err_msg}", category='danger')
    return redirect(url_for('catalog_page'))


@app.route('/cart', methods=['GET', "POST"])
@login_required
def cart_page():
    checkout_form = CheckoutForm()
    checkout_form.country.choices = [(country.id, country.name) for country in Country.query.all()]
    checkout_form.city.choices = [(city.id, city.name) for city in City.query.all()]
    products, total_cart = handle_cart()

    if checkout_form.validate_on_submit():
        total_quantity = sum([p['quantity'] for p in products])
        order = Order()
        checkout_form.populate_obj(order)
        order.country = str(Country.query.get(checkout_form.country.data))
        order.city = str(City.query.get(checkout_form.city.data))
        order.status = 'PROCESSING'
        order.total_quantity = total_quantity

        for product in products:
            order_item = OrderItems(product_id=product['id'], quantity=product['quantity'])
            order.items.append(order_item)

        db.session.add(order)
        db.session.commit()
        return redirect(url_for('succeed_order'))

    else:
        for err_msg in checkout_form.errors.values():
            flash(f"Error with creating user: {err_msg}", category='danger')

    return render_template('cart.html', items=products, total_cart=total_cart, checkout_form=checkout_form)


@app.route('/succeed-order')
@login_required
def succeed_order():
    return render_template('order_success.html')


@app.route('/remove-from-cart/<index>')
def remove_from_cart(index):
    del session['cart'][int(index)]
    session.modified = True
    return redirect(url_for('cart_page'))



@app.route('/get_cities/<int:country_id>', methods=['GET'])
def get_cities(country_id):
    cities = City.query.filter_by(country_id=country_id).all()
    cities_data = [{'id': city.id, 'name': city.name} for city in cities]
    return jsonify({'cities': cities_data})