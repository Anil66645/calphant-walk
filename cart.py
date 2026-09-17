def total(items):
    """Sum price * quantity for each (price, quantity) pair."""
    return sum(price * quantity for price, quantity in items)


def item_count(cart):
    """Sum the quantity of each (price, quantity) pair in the cart."""
    return sum(quantity for price, quantity in cart)
