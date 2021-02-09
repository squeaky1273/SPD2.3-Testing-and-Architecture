# Adapted from a Java code in the "Refactoring" book by Martin Fowler.
# Replace temp with query
# Code snippet. Not runnable.
"""DONE"""
def get_price():
    if base_price() > 1000: 
        discount_factor = 0.95
    else: 
        discount_factor = 0.98
    return base_price() * discount_factor

def base_price():
    return quantity * item_price

def discount_factor():
    return 0