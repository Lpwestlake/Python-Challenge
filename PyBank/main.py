import os
import csv 

budget_path = os.path.join("Resources/budget_data.csv")


# C:\Users\westl\Desktop\Python-Challenge\Python-Challenge\PyBank\Resources\budget_data.csv

with open(budget_path, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    for row in csv_reader:
        print(row)
    