#import dependencies
import os
import csv

#Define path to csv
csvpath = os.path.join('Resources', 'budget_data.csv')

#Create variable for holding csv columns as lists
date = []
prof_loss = []

#Open csv
with open(csvpath, newline='') as csvfile:

    #Specify csv delimiter and variable
    csvreader = csv.reader(csvfile, delimiter=',')

    #Skip header
    header = next(csvreader)

    #Loop through csv
    for row in csvreader:

        #Add each Profit/Loss value to the list
        date.append(row[0])
        prof_loss.append(int(row[1]))
   
#Determine the length of the date list to find the number of months
tot_months = len(date)

#Sum up the list of oto get the total
total_pl = sum(prof_loss)

#Calculate the average Profit/Losses
average = total_pl / tot_months
average = str(round(average, 2))

# #Find the greatest increase of prof_loss list
increase = max(prof_loss)
increase_position = prof_loss.index(increase)
increase_day = date[increase_position]

#Find the greatest decrease of prof_loss list
decrease = min(prof_loss)
decrease_position = prof_loss.index(decrease)
decrease_day = date[decrease_position]

#Print to terminal
summary = f'Total Months:{tot_months}\nTotal Profit/Losses: ${total_pl}\nAverage Profit/Losses: ${average}\nGreatest Increase in Revenue:{increase_day} ${increase}\nGreatest Decrease in Revenue:{decrease_day} ${decrease}'
print(summary)

#create and print to text file
fh = open('budget.txt', 'w')

fh.write(summary)

fh.close()
