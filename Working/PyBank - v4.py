# import modules
import os
import csv

# Define CSV Path 

csvpath = os.path.join ("c:/", "Users", "Suhaib Kiani", "Desktop", "Columbia Engineering", "Homework", "Homework 3 - Python", "Python-Challenge-", "PyBank", "budget_data.csv")

with open(csvpath, newline='') as csvfile:

# CSV reader specifies delimiter and variable that holds contents (f, delimiter="\t")
    csvreader = csv.DictReader(csvfile, delimiter="\t")
    
# Read the header row first (skip this part if there is no header)
    csv_header = next(csvfile)

profits = [float(row[1]) for row in csvreader]
    total_profit = sum(profits)  
    row_count = len(profits)
    average = sum(profits) / len(profits)

print ("________________________")
print ("Financial Analysis")
print ("________________________")
print(f"Total : {str(total_profit)}")
print(f"Total : {str(row_count)}")