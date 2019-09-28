#import dependencies
import os
import csv

#Define path to csv
csvpath = os.path.join('Resources', 'election_data.csv')

votes = []
khan = []
correy = []
li = []
otooley = []

#Open csv
with open(csvpath, newline='') as csvfile:

    #Specify csv delimiter and variable
    csvreader = csv.reader(csvfile, delimiter=',')

    #Skip header
    header = next(csvreader)

    #Loop through csv
    for row in csvreader:
        
        #Add each voter id to the list
        votes.append(row[0])

        #Add each vote for Khan
        if row[2] == "Khan":
            khan.append(row[2])

        if row[2] == "Correy":
            correy.append(row[2])

        if row[2] == "Li":
            li.append(row[2])

        if row[2] == "O'Tooley":
            otooley.append(row[2])

total_votes = len(votes)
khan_votes = len(khan)
khan_prct = str(round(khan_votes / total_votes * 100, 2))
correy_votes = len(correy)
correy_prct = str(round(correy_votes / total_votes * 100, 2))
li_votes = len(li)
li_prct = str(round(li_votes / total_votes * 100, 2))
otooley_votes = len(otooley)
otooley_prct = str(round(otooley_votes / total_votes * 100, 2))

results = '''Election Results\n 
--------------------------\n 
Total Votes: {total_votes}\n 
--------------------------\n 
Khan: {khan_prct}% ({khan_votes})\n 
Correy: {correy_prct}% ({correy_votes})\n 
Li: {li_prct}% ({li_votes})\n 
O\'Tooley: {otooley_prct}% ({otooley_votes})'''

print(results)

