import os
import csv 

csvpath = os.path.join("Resources/budget_data.csv")


# C:\Users\westl\Desktop\Python-Challenge\Python-Challenge\PyBank\Resources\budget_data.csv

with open(csvpath, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csv_reader)

# define lists
    month = []
    revenue = []
    revenue_change = []
    monthly_change = []

# define variables
    month_count = 0
    total_revenue = 0
    previous_revenue = 0
    #print(f'header: {csv_header}')

# create for loop
    for row in csv_reader:
        month.append(row[0])
        revenue.append(row[1])
        month_count += 1
        #print(month_count)
        total_revenue = total_revenue + int(row[1])
        #print(total_revenue)

        current_revenue = int(row[1])
        monthly_revenue_change = current_revenue - previous_revenue
        previous_revenue = current_revenue

        monthly_change.append(monthly_revenue_change)
        print(monthly_revenue_change)



# avg_monthly_change = sum(monthly_revenue_change) / len(month)
# print(avg_monthly_change)



        














#set counter and running calculation to 0 and create lists to store data
    # count = 0
    # totalProfit = 0
    # previousRev = 0
    # revChange = 0
    # averageChange = 0
    # monthChange = []
    # revChangeList = []
    
    # for row in csv_reader:      
    #     #this will count number of months
    #     count = count + 1
    #     #this will calculate the total profit/loss
    #     totalProfit = totalProfit + int(row[1])
    #     # # Add number months
    #     # monthChange.append(row[0])
    #     # # Add profit/loss amounts
    #     revChangeList = revChange.append(row[1])

    #     #prior Change = int(row[1])
    #     revChange = int(row[1]) - previousRev
    #     previousRev = int(row[1])
    #     monthChange = monthChange + int(row[0]

    # something = sum(revChange) / len(revChange)
    # print(averageChange)


    #     final_profit = int(row[1])
    #     monthly_change_profits = final_profit - initial_profit

    #   #Store these monthly changes in a list
    #     monthly_changes.append(monthly_change_profits)

    #     total_change_profits = total_change_profits + monthly_change_profits
    #     initial_profit = final_profit

    #     #Calculate the average change in profits
    #     average_change_profits = (total_change_profits/count)
        
    #     #Find the max and min change in profits and the corresponding dates these changes were obeserved
    #     greatest_increase_profits = max(monthly_changes)
    #     greatest_decrease_profits = min(monthly_changes)

    #     increase_date = date[monthly_changes.index(greatest_increase_profits)]
    #     decrease_date = date[monthly_changes.index(greatest_decrease_profits)]
    
            
    ## Add Print Statments
    #print(count)
    #print(totalProfit)

