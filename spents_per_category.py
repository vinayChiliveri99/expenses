""" This module contains a function to calculate the
total spents from each category from the cleaned expenses. """


def get_spents_per_category(expenses):
    """ calculate the total spents from each category from the cleaned expenses """
    spents_per_category = {}
    for expense in expenses:
        category = expense['category']
        # .get() returns 0 the first time a category is seen,
        # so we don't need a separate if/else
        spents_per_category[category] = spents_per_category.get(category, 0) + expense['amount']
    return spents_per_category
