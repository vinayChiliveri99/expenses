""" This module contains the main function to calculate the total amount 
spent from the expenses.csv file. """

from total_spents import get_total_spent
from spents_per_category import get_spents_per_category
from top_3_expenses import get_top_3_expenses
from total_no_of_transactions import get_total_transactions

def main():
    """ main function to call other functions """
    total_spent = get_total_spent()
    print(f'Total amount spent: ₹{total_spent}')

    spents_per_category = get_spents_per_category()
    print("\nSpending per category:")
    # print(spents_per_category)
    for category, amount in spents_per_category.items():
        print(f"  {category.capitalize()}: ₹{amount}")

    top_3_expenses = get_top_3_expenses()
    print("\nTop 3 expenses:")
    for category, amount in top_3_expenses:
        print(f"  {category.capitalize()}: ₹{amount}")


    print('Total Transactions:', get_total_transactions())


if __name__ == "__main__":
    main()

# In Python, defining a function doesn't automatically execute it. You have defined main(), '
# 'but you haven't called it anywhere.

# Unlike some languages, Python doesn't automatically execute a function named main.

# This main guard ensures that main() executes only when this file
# is run directly, and not when it is imported as a module into another file.
