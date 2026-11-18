""" This module contains a function to calculate the
total number of transactions from the expenses.csv file. """
import csv

def get_total_transactions():
    """ calculate the total number of transactions from the expenses.csv file """
    with open('expenses.csv', mode='r', newline='', encoding='utf-8') as file:
        # since the rows are tab-seperated,
        # we need to specify the delimiter as '\t', default is comma ','
        reader = csv.DictReader(file, delimiter='\t')
        # remove empty rows and count the number of transactions
        return sum(1 for row in reader if (row.get('date')).strip())
