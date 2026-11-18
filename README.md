# Expenses Report

A small Python drill: read a deliberately messy `expenses.csv` using only the
standard-library `csv` module, clean it, and print a spending report.

## Run it

```bash
python3 expenses.py
```

It works from any directory, because the CSV path is built from the script's own location.

## Sample output

```
Total amount spent: ₹20,367.00

Spending per category:
  Food: ₹7,030.00
  Transport: ₹2,470.00
  Utilities: ₹3,299.00
  Health: ₹2,440.00
  Entertainment: ₹1,199.00
  Shopping: ₹3,929.00

Top 3 expenses:
  2026-11-17  Shoes (Shopping): ₹2,799.00
  2026-11-04  Electricity bill (Utilities): ₹2,450.00
  2026-11-11  Groceries (Food): ₹2,100.00

Total Transactions: 21
Skipped (blank amount): 3
Skipped (duplicate row): 1
```

## The data

`expenses.csv` has 25 rows with the columns `date, description, amount, category`.
It is messy on purpose:

| Mess | Example | How it's handled |
|---|---|---|
| Blank amounts | `2026-11-03,Coffee,,Food` | Skipped and counted |
| Rupee symbol and commas | `"₹1,200"` | `₹` and `,` are removed, then the value goes through `float()` |
| Mixed-case categories | `Food`, `FOOD`, `food` | Lowercased before grouping |
| One exact duplicate row | `Restaurant dinner` on 2026-11-13 | Second copy skipped and counted |

Amounts that contain a comma, such as `"₹1,200"`, must be wrapped in double quotes.
Without the quotes, the comma would split the value into two columns. `csv.DictReader`
removes the quotes automatically.

Two `Groceries ₹1,200` rows on different dates are **not** duplicates. They are two
separate purchases. A row counts as a duplicate only when every column matches.

## Project layout

| File | Purpose |
|---|---|
| `expenses.py` | Entry point. Loads the data once and prints the report |
| `load_expenses.py` | Reads and cleans the CSV in one pass. All cleaning logic lives here |
| `total_spents.py` | `get_total_spent(expenses)`: sum of all amounts |
| `spents_per_category.py` | `get_spents_per_category(expenses)`: `{category: total}` dict |
| `top_3_expenses.py` | `get_top_3_expenses(expenses)`: three largest rows, sorted with a key function |
| `total_no_of_transactions.py` | `get_total_transactions(expenses)`: count of valid rows |

The CSV is read once in `load_expenses()`. Every other function receives the cleaned list
as input, so a cleaning fix only ever needs to be made in one place.

## Concepts practised

- `csv.DictReader` with `newline=''` and `encoding='utf-8'`
- Data cleaning with `str.replace`, `str.strip` and `try/except ValueError`
- Removing duplicates with a `set` of tuples (dicts can't go into a set, but tuples can)
- Grouping with `dict.get(key, 0)`
- Sorting with `sorted(..., key=get_amount, reverse=True)`
- Formatting money with an f-string: `f'₹{amount:,.2f}'`
- The `if __name__ == "__main__":` guard

## Constraints

No pandas and no third-party packages. Only `csv` is used for parsing. `os` is used only
to find the CSV next to the script.
