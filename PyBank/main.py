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

        #Count the months
        date.append(row[0])

        #Add each Profit/Loss value to the list
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
print('Financial Analysis')
print('------------------------------')
print(f'Total Months:{tot_months}')
print(f'Total Profit/Losses: ${total_pl}')
print(f'Greatest Increase in Revenue:{increase_day} ${increase}')
print(f'Greatest Decrease in Revenue:{decrease_day} ${decrease}')

#Create and print to text file
fh = open('budget.txt', 'w')

fh.write('Financial Analysis\n')
fh.write('------------------------------\n')
fh.write(f'Total Months:{tot_months}\n')
fh.write(f'Total Profit/Losses: ${total_pl}\n')
fh.write(f'Greatest Increase in Revenue:{increase_day} ${increase}\n')
fh.write(f'Greatest Decrease in Revenue:{decrease_day} ${decrease}')

fh.close()