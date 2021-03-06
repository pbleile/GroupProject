from config import app
from controllers import *

## master routes ##
# Restaurant Welcome page
app.add_url_rule('/', view_func=index)
# Customer Login
app.add_url_rule('/user/login', view_func=show_login)
app.add_url_rule('/user/do_login',view_func=do_login,methods=['POST'])

# Customer Registration
app.add_url_rule('/user/register', view_func=show_registration)
app.add_url_rule('/user/do_registration', view_func=do_registration,methods=['POST'])

# Customer dashboard
app.add_url_rule('/nav', view_func=nav)
app.add_url_rule('/logout', view_func=logout)
app.add_url_rule('/create',view_func=show_custompizza)
app.add_url_rule('/random',view_func=random_pizza)
app.add_url_rule('/add_pizza',view_func=add_pizza,methods=['POST'])
app.add_url_rule('/checkout',view_func=show_checkout)
app.add_url_rule('/charge',view_func=charge,methods=['POST'])
app.add_url_rule('/total',view_func=get_order_total)

## Order edits
app.add_url_rule('/remove/<id>/order', view_func=start_over)
app.add_url_rule('/remove/pizza',view_func=delete_pizza,methods=['POST'])
app.add_url_rule('/remove/pizzas',view_func=clear_order,methods=['POST'])

## customer routes
app.add_url_rule('/quick', view_func=quick)
app.add_url_rule('/account', view_func=cust_account)
app.add_url_rule('/account/update', view_func=cust_update, methods=['POST'])
app.add_url_rule('/favorite',view_func=reorder_favorite)
app.add_url_rule('/favorite/update',view_func=make_favorite,methods=['POST'])
app.add_url_rule('/ordertype',view_func=set_order_type,methods=['POST'])
app.add_url_rule('/danger',view_func=show_danger)
