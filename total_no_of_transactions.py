""" This module contains a function to calculate the
total number of valid transactions from the cleaned expenses. """


def get_total_transactions(expenses):
    """ count the transactions that have an amount and are not duplicates """
    # blank amounts and duplicates were already removed in load_expenses
    return len(expenses)
