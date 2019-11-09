# import modules
import os
import csv

# Define CSV Path 

csvpath = os.path.join ("c:/", "Users", "Suhaib Kiani", "Desktop", "Columbia Engineering", "Homework", "Homework 3 - Python", "Python-Challenge-", "PyBank", "budget_data.csv")

with open(csvpath, newline='') as csvfile:

# CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
# Read the header row first (skip this part if there is no header)
    csv_header = next(csvfile)


#Sum of Column 1 (Attempt A)
    total_profit = 0
    
    for row in csvreader:
        month_profit = float(row[1])
        total_profit = month_profit + total_profit 
            
    row_count = sum(1 for row in csvreader)


print ("________________________")
print ("Financial Analysis")
print ("________________________")
print(f"Total : {str(total_profit)}")
print(f"Total : {str(row_count)}")