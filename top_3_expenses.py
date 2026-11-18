""" This module contains a function to find the
top 3 expenses from the cleaned expenses. """


def get_amount(expense):
    """ key function for sorting: return the amount of an expense """
    return expense['amount']


def get_top_3_expenses(expenses):
    """ return the 3 biggest expenses, keeping the whole row
    so the description can be printed too """
    # sorted() returns a new list and leaves the original untouched
    return sorted(expenses, key=get_amount, reverse=True)[:3]
