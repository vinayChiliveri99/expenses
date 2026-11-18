""" This module contains a function to calculate the
top 3 expenses from the expenses.csv file. """
import csv

def get_top_3_expenses():
    """ calculate the top 3 expenses from the expenses.csv file """
    with open('expenses.csv', mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter='\t')
        expenses = []
        for row in reader:
            if row['amount'] != '':
                amount = float(row['amount'].replace(',', '').replace('₹', ''))
                expenses.append((row['category'].lower(), amount))


    # Sort expenses by amount in descending order and return the top 3
    expenses.sort(key=lambda x: x[1], reverse=True)
    return expenses[:3]
