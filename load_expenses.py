""" This module contains a function to read and clean the rows
of the expenses.csv file. Every other module works on its output,
so the cleaning logic lives in one place only. """

import csv
import os

# build the path from this file's location, so the script works
# no matter which directory it is run from
CSV_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'expenses.csv')


def parse_amount(raw_amount):
    """ convert a messy amount like '₹1,200' into a float,
    return None if the amount is blank or not a number """
    cleaned = raw_amount.replace('₹', '').replace(',', '').strip()
    if cleaned == '':
        return None
    try:
        return float(cleaned)
    except ValueError:
        # values like 'N/A' or 'abc' are treated as missing
        return None


def load_expenses(path=CSV_PATH):
    """ read the csv file once and return a tuple of
    (expenses, skipped_blank, skipped_duplicate), where expenses
    is a list of clean dicts """
    expenses = []
    seen_rows = set()
    skipped_blank = 0
    skipped_duplicate = 0

    with open(path, mode='r', newline='', encoding='utf-8') as file:
        # the file is comma-separated; amounts like "₹1,200" are wrapped
        # in quotes, and csv handles the quotes for us
        reader = csv.DictReader(file)
        for row in reader:
            # strip spaces from every value; 'or' handles None for short rows
            row = {key: (value or '').strip() for key, value in row.items()}

            # ignore completely empty lines
            if not any(row.values()):
                continue

            # a row is a duplicate only if every column matches exactly;
            # dicts can't go into a set, but tuples can
            row_key = tuple(row.values())
            if row_key in seen_rows:
                skipped_duplicate += 1
                continue
            seen_rows.add(row_key)

            amount = parse_amount(row['amount'])
            if amount is None:
                skipped_blank += 1
                continue

            expenses.append({
                'date': row['date'],
                'description': row['description'],
                'amount': amount,
                'category': row['category'].lower(),
            })

    return expenses, skipped_blank, skipped_duplicate
