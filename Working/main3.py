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

# Define the function and have it accept the 'wrestler_data' as its sole parameter
def print_percentages(csvreader):
    # For readability, it can help to assign your values to variables with descriptive names
    date = str(csvreader[0])
    profit = int(csvreader[1])
    


    for column in csv_header:
        profit = int(sum(column[1]))

    # average of changes in profits/losses
    avg_profit = profit/row_count


print ("Financial Analysis")
print ("________________________")
print(f"Total Months: {row_count}")
