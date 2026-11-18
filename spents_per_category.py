""" This module contains a function to calculate the
total spents from each category from the expenses.csv file. """

import csv

def get_spents_per_category():
    """ calculate the total spents from each category from the expenses.csv file """
    with open('expenses.csv', mode = 'r', newline = '', encoding = 'utf-8') as file:
        # since the rows are tab-seperated,
        # we need to specify the delimiter as '\t', default is comma ','
        reader = csv.DictReader(file, delimiter = '\t')
        spents_per_category = {}
        for row in reader:
            if row['amount'] != '':
                category = row['category'].lower()
                amount = float(row['amount'].replace(',', '').replace('₹', ''))
                if category in spents_per_category:
                    spents_per_category[category] += amount
                else:
                    spents_per_category[category] = amount
    return spents_per_category
