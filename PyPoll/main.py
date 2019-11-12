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

# Define Initial Variables (not sure on how to define strings for the months)
    total_votes = 0
    vote_count = 0
    Khan = 0
    Correy = 0
    Li = 0
    Tooley = 0
    Winner = "NA"
    

# Initiate loop 
    for row in csvreader:  

# A: Intilize a null list to identify unique candidates 
        candidate_list = [] 
        candidate = str(row[2])

    # traverse for all elements, check if exists in unique_list or not and append if not 
        if candidate not in candidate_list: 
            candidate_list.append(candidate) 
    
# B: Calculate Votes and determine winner
   
        if str(row[2]) == str("Khan"):
            total_votes = total_votes + 1
            Khan = Khan + 1
            if Khan >= max(Khan, Correy, Li, Tooley): 
               Winner = "Khan"   

        if str(row[2]) == str("Correy"):
            total_votes = total_votes + 1
            Correy = Correy + 1
            if Correy >= max(Khan, Correy, Li, Tooley): 
               Winner = "Correy"   

        if str(row[2]) == str("Li"):
            total_votes = total_votes + 1
            Li = Li + 1
            if Li >= max(Khan, Correy, Li, Tooley): 
               Winner = "Li"   

        if str(row[2]) == str("O'Tooley"):
            total_votes = total_votes + 1
            Tooley = Tooley + 1
            if Tooley >= max(Khan, Correy, Li, Tooley): 
               Winner = "O'Tooley"   
        
# B: Calculate Percentages  
    Khan_cent = int((Khan / total_votes) * 100)
    Correy_cent = int((Correy / total_votes) * 100)
    Li_cent = int((Li / total_votes) * 100)
    Tooley_cent= int((Tooley / total_votes) * 100)
    
# C: Output to Terminal   
print ("--------------------------------------")
print ("Election Results")
print ("--------------------------------------")
print(f"Total Votes: {total_votes}")
print ("--------------------------------------")
print(f"Khan: {Khan_cent}{'%'} ({Khan})")
print(f"Correy: {Correy_cent}{'%'} ({Correy})")
print(f"Li: {Li_cent}{'%'} ({Li})")
print(f"Tooley: {Tooley_cent}{'%'} ({Tooley})")
print ("--------------------------------------")
print(f"Winner: {Winner}")
print ("--------------------------------------")


# D: Write the results to an output TXT file   
txt_file = open("pypoll_results.txt","w")    

dotted_line = str("___________ \n") 
txt_file.writelines(dotted_line)
txt_file.write("Election Results \n")
txt_file.writelines(dotted_line)

L = [f"Total Votes: {total_votes}","\n"] 
txt_file.writelines(L)
txt_file.writelines(dotted_line)

M = [f"Khan: {Khan_cent}{'%'} ({Khan})","\n"]
txt_file.writelines(M)
N = [f"Correy: {Correy_cent}{'%'} ({Correy})","\n"]
txt_file.writelines(N)
O = [f"Li: {Li_cent}{'%'} ({Li})","\n"]
txt_file.writelines(O)
P = [f"Tooley: {Tooley_cent}{'%'} ({Tooley})","\n"]
txt_file.writelines(P)

txt_file.writelines(dotted_line)
W = [f"Winner: {Winner}","\n"]
txt_file.writelines(W)
txt_file.writelines(dotted_line)

txt_file.close()