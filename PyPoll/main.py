# import modules
import os
import csv

# Define CSV Path 
csvpath = os.path.join ("c:/", "Users", "Suhaib Kiani", "Desktop", "Columbia Engineering", "Homework", "Homework 3 - Python", "Python-Challenge-", "PyPoll", "election_data.csv")

with open(csvpath, newline='') as csvfile:


# CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvfile)

# intilize a null list 
    unique_list = [] 

    # traverse for all elements 
    for row in csvreader:
        candidate = str(row[2])
    # check if exists in unique_list or not 
        if candidate not in unique_list: 
            unique_list.append(candidate) 
    



# Total vote count 
    #row_count = sum(1 for row in csvreader)
row_count = len(row[0])

# function to get unique values of candidate names 

      


 
#output  
print ("")
print ("Election Results")
print ("________________________")
print(f"Total Votes: {row_count}")
print ("________________________")
print(unique_list)
print ("________________________")
print(len(unique_list))
print(f"Header: {csv_header}")
