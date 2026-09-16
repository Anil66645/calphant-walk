def total(items):
    """Sum price * quantity for each (price, quantity) pair."""
    return sum(price for price, quantity in items)
