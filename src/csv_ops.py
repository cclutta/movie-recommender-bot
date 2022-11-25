#!/usr/bin/python3
""" CSV operations module
"""
from csv import writer
from datetime import datetime

ratings_file = "data/ratings.csv"

def add_rating_row(row_list):
    """
    Append the row we want to add as a list
    """
    with open(ratings_file, 'a') as f:
        w_object = writer(f)
        w_object.writerow(row_list)
        f.close()


if __name__ == "__main__":

    row_list = [799, 1, 5]
    ct = datetime.now()
    row_list.append(int(ct.timestamp()))
    try:
        add_rating_row(row_list)
    except Exception:
       print("Error saving rating! Please try again.")
    
