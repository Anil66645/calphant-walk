def total(items):
    """Sum price * quantity for each (price, quantity) pair."""
    return sum(price * quantity for price, quantity in items)
