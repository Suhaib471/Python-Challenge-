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


    # row count 
    row_count = sum(1 for row in csvreader)

#Sum of Column 1 (Attempt A)
    #xs = 0
    #for row in csvreader:
    #        x = float(row[1])
    #        xs=xs + x 

# average of changes in profits/losses
    

print ("Financial Analysis")
print ("________________________")
print(f"Total Months: {row_count}")
print(xs)
print(f"Header: {csv_header}")

