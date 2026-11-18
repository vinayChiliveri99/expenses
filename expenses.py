""" This module contains the main function that reads expenses.csv once
and prints the total spend, spend per category and the top 3 expenses. """

from load_expenses import load_expenses
from total_spents import get_total_spent
from spents_per_category import get_spents_per_category
from top_3_expenses import get_top_3_expenses
from total_no_of_transactions import get_total_transactions


def format_rupees(amount):
    """ format a number as rupees with commas and 2 decimals, e.g. ₹1,200.00 """
    return f'₹{amount:,.2f}'


def main():
    """ main function to call other functions """
    # read and clean the file only once, then pass the list around
    expenses, skipped_blank, skipped_duplicate = load_expenses()

    total_spent = get_total_spent(expenses)
    print(f'Total amount spent: {format_rupees(total_spent)}')

    spents_per_category = get_spents_per_category(expenses)
    print("\nSpending per category:")
    # print(spents_per_category)
    for category, amount in spents_per_category.items():
        print(f"  {category.capitalize()}: {format_rupees(amount)}")

    top_3_expenses = get_top_3_expenses(expenses)
    print("\nTop 3 expenses:")
    for expense in top_3_expenses:
        print(f"  {expense['date']}  {expense['description']} "
              f"({expense['category'].capitalize()}): {format_rupees(expense['amount'])}")

    print('\nTotal Transactions:', get_total_transactions(expenses))
    print('Skipped (blank amount):', skipped_blank)
    print('Skipped (duplicate row):', skipped_duplicate)


if __name__ == "__main__":
    main()

# In Python, defining a function doesn't automatically execute it. You have defined main(), '
# 'but you haven't called it anywhere.

# Unlike some languages, Python doesn't automatically execute a function named main.

# This main guard ensures that main() executes only when this file
# is run directly, and not when it is imported as a module into another file.
