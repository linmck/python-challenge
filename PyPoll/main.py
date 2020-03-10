#import dependencies
import os
import csv

#Define path to csv
election_data_path = os.path.join('Resources', 'election_data.csv')

votes = []
khan = []
correy = []
li = []
otooley = []

#Open csv
with open(election_data_path, newline='') as csvfile:

    #Specify csv delimiter and variable
    csvreader = csv.reader(csvfile, delimiter=',')

    #Skip header
    header = next(csvreader)

    #Loop through csv
    for row in csvreader:
        
        #Add each voter id to the list
        votes.append(row[2])

        #Add each vote for Khan
        if row[2] == "Khan":
            khan.append(row[2])

        if row[2] == "Correy":
            correy.append(row[2])

        if row[2] == "Li":
            li.append(row[2])

        if row[2] == "O'Tooley":
            otooley.append(row[2])

#Calculate the total number of votes
total_votes = len(votes)

#Calculate the total number and percentage of Khan votes
khan_votes = len(khan)
khan_prct = khan_votes / total_votes

#Calculate the total number and percentage of Correy votes
correy_votes = len(correy)
correy_prct = correy_votes / total_votes

#Calculate the total number and percentage of Li votes
li_votes = len(li)
li_prct = li_votes / total_votes

#Calculate the total number and percentage of O'Tooley votes
otooley_votes = len(otooley)
otooley_prct = otooley_votes / total_votes

#Create dictionary to compare votes and find winner
candidates = {'Khan':khan_votes, 'Correy':correy_votes, 'Li':li_votes, 'O\'Tooley':otooley_votes}
winner = max(candidates, key=candidates.get)

#Print to terminal
print('Election Results')
print('------------------------------')
print(f'Total Votes:{total_votes}')
print('------------------------------')
print(f'Khan: {khan_prct:.2%} ({khan_votes})') 
print(f'Correy: {correy_prct:.2%} ({correy_votes})')
print(f'Li: {li_prct:.2%} ({li_votes})')
print(f'O\'Tooley: {otooley_prct:.2%} ({otooley_votes})')
print('------------------------------')
print(f'Winner: {winner}')
print('------------------------------')

#Create and print to text file
fh = open('poll.txt', 'w')

fh.write('Election Results\n')
fh.write('------------------------------\n')
fh.write(f'Total Votes:{total_votes}\n')
fh.write('------------------------------\n')
fh.write(f'Khan: {khan_prct:.2%} ({khan_votes})\n') 
fh.write(f'Correy: {correy_prct:.2%} ({correy_votes})\n')
fh.write(f'Li: {li_prct:.2%} ({li_votes})\n')
fh.write(f'O\'Tooley: {otooley_prct:.2%} ({otooley_votes})\n')
fh.write('------------------------------\n')
fh.write(f'Winner: {winner}\n')
fh.write('------------------------------\n')

fh.close()

