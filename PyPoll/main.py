import os
import csv 

csvpath = os.path.join("Resources/election_data.csv")


# C:\Users\westl\Desktop\Python-Challenge\Python-Challenge\PyBank\Resources\budget_data.csv

with open(csvpath, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csv_reader)

    