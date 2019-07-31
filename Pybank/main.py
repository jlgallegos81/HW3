#Import modules

import os
import csv

#Set Variables
date = []
profit_loses = []
monthly_change = []
total_revenue = 0
initial_profit = 0 
month_count = 0
total_profit_change = 0

#Filepath
csvpath = os.path.join("Resources", "budget_data.csv")

#Read the CSV, loop, pull data into lists, count total months.
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        month_count = month_count + 1
        date.append(row[0])
        profit_loses.append(int(row[1]))
        total_revenue = total_revenue + int(row[1])
        profit = int(row[1])
        monthly_change_profit = profit - initial_profit
        monthly_change.append(monthly_change_profit)
        
    #Find profit average and changes
    total_profit_change = total_profit_change + monthly_change_profit
    initial_profit = profit
    average_change = (total_profit_change/month_count)

    #Find the highest and lowest profits amounts and months
    largest_increase = max(monthly_change)
    largest_decrease = min(monthly_change)

    increase_date = date[monthly_change.index(largest_increase)]
    decrease_date = date[monthly_change.index(largest_decrease)]

    #Show work
    print("**************************************************")  
    print("Check this shit out")
    print("--------------------------------------------------")
    print("Total Months: " + str(month_count))
    print("Total Profits: " + "$" + str(total_revenue))
    print("Average Change: " + "$" + str(int(average_change)))
    print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(largest_increase) + ")")
    print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(largest_decrease)+ ")")
    print("**************************************************")
#Output to file
with open("pybank.txt", "w") as text:
    text.write("**************************************************\n") 
    text.write("Check this shit out"+ "\n")
    text.write("--------------------------------------------------\n")
    text.write("Total Months: " + str(month_count) + "\n")
    text.write("Total Profits: " + "$" + str(total_revenue) +"\n")
    text.write("Average Change: " + '$' + str(int(average_change)) + "\n")
    text.write("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(largest_increase) + ")\n")
    text.write("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(largest_decrease) + ")\n")
    text.write("**************************************************")




