from src.shop import Product, Order


def test_creating_product_with_default_quantity():
    test_product = Product('Shoes', 100.0)
    assert test_product.unit_price == 100.0
    assert test_product.quantity == 1.0
    assert test_product.name == 'Shoes'
    assert test_product.get_price() == 100.00


def test_creating_product_with_quantity_larger_than_default():
    test_product = Product('Shoes', 30.00, 3.0)
    assert test_product.unit_price == 30.00
    assert test_product.quantity == 3.0
    assert test_product.name == 'Shoes'
    assert test_product.get_price() == 90.00


def test_order_with_no_products():
    test_order = Order('adrian@example.com')
    assert test_order.customer_email == 'adrian@example.com'
    assert test_order.get_total_price() == 0


def test_order_with_one_product():
    test_order = Order('adrian@example.com')
    test_product = Product('Shoes', 30.00, 3.0)
    test_order.add_product(test_product)
    assert test_order.get_total_price() == 90


def test_order_with_three_products():
    test_order = Order('adrian@example.com')
    shoes = Product('Shoes', 30.00, 3.0)
    tshirt = Product('T-Shirt', 50.00, 2.0)
    bag = Product('Bag', 10.00)
    test_order.add_product(shoes)
    test_order.add_product(tshirt)
    test_order.add_product(bag)
    assert test_order.get_total_price() == 200.0
    assert test_order.get_total_quantity_of_products() == 6


def test_order_purchase():
    test_order = Order('adrian@example.com')
    shoes = Product('Shoes', 30.00, 3.0)
    test_order.add_product(shoes)
    test_order.purchase()
    assert test_order.purchased
