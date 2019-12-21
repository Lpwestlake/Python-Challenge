import os
import csv 

# define read path (run from Python-Challenge folder)
csvpath = os.path.join("PyBank", "Resources/budget_data.csv")

# define write path for output (run from Python-Challenge folder)
output_path = os.path.join("Pybank", "Output/PyBank.txt")

# C:\Users\westl\Desktop\Python-Challenge\Python-Challenge\PyBank\Resources\budget_data.csv

with open(csvpath, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
# designate header row
    csv_header = next(csv_reader)

# define lists
    month = []
    revenue = []
    revenue_change_list = []

# define variables
    month_count = 0
    total_revenue = 0

# define first row so changes calculation can skip first row change from 0 (similar to a 'look ahead')
    first_row = next(csv_reader)
    previous_revenue = int(first_row[1])
    month_count = month_count + 1
    total_revenue = total_revenue + int(first_row[1])

# create for loop
    for row in csv_reader:
    # calculate total months and total revenue    
        month_count = month_count + 1
        total_revenue = total_revenue + int(row[1])

    # create list of profit/loss changes for each row
        revenue_change = int(row[1])-previous_revenue
        revenue_change_list.append(revenue_change)
        previous_revenue = int(row[1])

    # greatest increase in profits
        if revenue_change == max(revenue_change_list):
           max_month = row[0]
           
    # greatest decrease (lowest increase) in profits 
        if revenue_change == min(revenue_change_list):
           min_month = row[0]
          
# calculate averae of changes in revenue
avg_change = sum(revenue_change_list)/len(revenue_change_list)
greatest_increase = max(revenue_change_list)
greatest_decrease = min(revenue_change_list)
  
# generate print statmeents
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {str(month_count)}")
print(f"Total: ${str(total_revenue)}")
print(f"Average Change: ${str(round(avg_change,2))}")
print(f"Greatest Increase in Profits: {max_month} (${str(greatest_increase)})")
print(f"Greatest Decrease in Profits: {min_month} (${str(greatest_decrease)})")

# open the file using "write" mode
with open(output_path, 'w') as txtfile:

# rite the print statements including '\n' to dictate end of line
    txtfile.write("Financial Analysis\n")
    txtfile.write("---------------------\n")
    txtfile.write(f"Total Months: {str(month_count)}\n")
    txtfile.write(f"Total: ${str(total_revenue)}\n")
    txtfile.write(f"Average Change: ${str(round(avg_change,2))}\n")
    txtfile.write(f"Greatest Increase in Profits: {max_month} (${str(greatest_increase)})\n")
    txtfile.write(f"Greatest Decrease in Profits: {min_month} (${str(greatest_decrease)})\n")

