""" This module contains a function to calculate the
total amount spent from the expenses.csv file. """

import csv

def get_total_spent():
    """ calculate the total amount spent from the expenses.csv file """
    with open('expenses.csv', mode='r', newline='', encoding='utf-8') as file:
        # since the rows are tab-seperated,
        # we need to specify the delimiter as '\t', default is comma ','
        reader = csv.DictReader(file, delimiter='\t')
        total_spent = 0
        for row in reader:
            if row['amount'] != '':
                total_spent += float(row['amount'].replace(',', '').replace('₹', ''))
        return int(total_spent)

