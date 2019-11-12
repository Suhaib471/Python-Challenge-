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

# Define Initial Variables (not sure on how to define strings for the months)
    total_profit = 0
    row_count = 0
    maximum_profit = 0
    maximum_month = str
    minimum_profit = 0
    minimum_month = str


# Set up for loop
    for row in csvreader:

# A: Calculation of Sum of Profit Column  
        month_profit = float(row[1])
        total_profit = month_profit + total_profit 
  
# B: Calculation of Total Months          
        row_count = row_count + 1

# C: Calculation of Average Change    
        average = total_profit / row_count

# D: Calculation of Maximum Profit
        if int(maximum_profit) < int(row[1]):
            maximum_profit = row[1] 
            maximum_month = row[0]

# E: Calculation of Minimum Profit
        if int(minimum_profit) > int(row[1]):
            minimum_profit = row[1] 
            minimum_month = row[0]

# F: Output to Terminal   
print ("-------------------------------")
print ("Financial Analysis")
print ("-------------------------------")
print(f"Total Months: {str(row_count)}")
print(f"Total : {str(total_profit)}")
print(f"Average Change : {int(average)}")
print(f"Greatest Increase in Profits : {str(maximum_month)} ({float(maximum_profit)})")
print(f"Greatest Decrease in Profits : {str(minimum_month)} ({float(minimum_profit)})")

# G: Write the results to an output TXT file
txt_file = open("pybank_results.txt","w")    

dotted_line = str("___________ \n") 
txt_file.writelines(dotted_line)
txt_file.write("Financial Analysis \n")
txt_file.writelines(dotted_line)

L = [f"Total Months: {str(row_count)}","\n"] 
txt_file.writelines(L)
M = [f"Total : {str(total_profit)}","\n"]
txt_file.writelines(M)
N = [f"Average Change : {int(average)}","\n"]
txt_file.writelines(N)
O = [f"Greatest Increase in Profits : {str(maximum_month)} ({float(maximum_profit)})","\n"]
txt_file.writelines(O)
P = [f"Greatest Decrease in Profits : {str(minimum_month)} ({float(minimum_profit)})","\n"]
txt_file.writelines(P)
txt_file.writelines(dotted_line)

txt_file.close()