def total(items):
    """Sum price * quantity for each (price, quantity) pair."""
    return sum(price * quantity for price, quantity in items)


def item_count(cart):
    """Sum the quantity of each (price, quantity) pair in the cart."""
    return sum(quantity for price, quantity in cart)


def is_empty(cart):
    """Return True when the cart has no items, False otherwise."""
    return item_count(cart) == 0


def has_price(cart, price):
    """Return True when any (price, quantity) pair in the cart has this price."""
    return any(item_price == price for item_price, quantity in cart)


def apply_discount(cart, percent):
    """Return the cart total reduced by percent.

    Raises ValueError when percent is below 0 or above 100.
    """
    if percent < 0 or percent > 100:
        raise ValueError("percent must be between 0 and 100")
    return total(cart) * (1 - percent / 100)
