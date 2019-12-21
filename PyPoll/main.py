import os
import csv 

csvpath = os.path.join("Pypoll", "Resources/election_data.csv")


# C:\Users\westl\Desktop\Python-Challenge\Python-Challenge\PyBank\Resources\budget_data.csv

with open(csvpath, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csv_reader)

    votes = 0
    candidates = []
    vote_count = []
    vote_percent = []

    for row in csv_reader:
        # month.append(row[0])
        # revenue.append(row[1])
        votes = votes + 1
        
        
        print(votes)
        #total_revenue = total_revenue + int(row[1])
        #print(total_revenue)

       
        # current_revenue = int(row[1])
        # revenue_change_list = current_revenue - previous_revenue
        # previous_revenue = current_revenue