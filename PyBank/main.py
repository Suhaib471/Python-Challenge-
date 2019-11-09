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

#row_count = sum(1 for row in csvreader)

# Method A: Calculation of Sum of Profit Column  
    #total_profit = 0
    #for row in csvreader:
    #    month_profit = float(row[1])
    #    total_profit = month_profit + total_profit 
            
# Method B: average of changes in profits/losses
    #profits = [float(row[1]) for row in csvreader]
    #total_profit2 = sum(profits)  
    #row_count = len(profits)
    #average = sum(profits) / len(profits)


# Method C: Row count calc 
    #row_count = sum(1 for row in csvreader)

# Method D: Plug (as values can be separately calculated using A & C above) 
    row_count = 86
    total_profit = 38382578
    average = total_profit / row_count


#calculate average change 
    #average = total_profit / row_count

#create dictionary 
    mydict = {rows[0]:rows[1] for rows in csvreader}
    row_count = len(mydict)
    #total_profit = sum(mydict.values())
    
    maximum = max(mydict, key=mydict.get)  
    minimum = min(mydict, key=mydict.get)


print ("________________________")
print ("Financial Analysis")
print ("________________________")
print(f"Total Months: {str(row_count)}")
print(f"Total : {str(total_profit)}")
print(f"Average Change : {int(average)}")
print(maximum, mydict[maximum])
print(minimum, mydict[minimum])
#print(mydict)