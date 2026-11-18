""" This module contains a function to calculate the
total amount spent from the cleaned expenses. """


def get_total_spent(expenses):
    """ calculate the total amount spent from the cleaned expenses """
    # no int() here, so paise are not silently dropped
    return sum(expense['amount'] for expense in expenses)
