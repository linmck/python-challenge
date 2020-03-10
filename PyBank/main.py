#import dependencies
import os
import csv

#Define path to csv
budget_path = os.path.join('Resources', 'budget_data.csv')

#Create variable for holding csv columns as lists
date = []
prof_loss = []

#Open csv
with open(budget_path, newline='') as csvfile:

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
tot_prof_loss = sum(prof_loss)

#Create variable to hold list of Changes captured with a for loop
changes = [prof_loss[i+1] - prof_loss[i] for i in range(len(prof_loss)-1)] 
tot_changes = sum(changes)
num_changes = len(changes)

#Calculate the average Profit/Losses
average = tot_changes / num_changes
average = str(round(average, 2))

# #Find the greatest increase of prof_loss list
increase = max(changes)
increase_position = changes.index(increase)
increase_day = date[(increase_position)+1]

#Find the greatest decrease of prof_loss list
decrease = min(changes)
decrease_position = changes.index(decrease)
decrease_day = date[(decrease_position)+1]

#Print to terminal
print('Financial Analysis')
print('------------------------------')
print(f'Total Months:{tot_months}')
print(f'Total Profit/Losses: ${tot_prof_loss}')
print(f'Average Profit/Loss Change: ${average}')
print(f'Greatest Increase in Revenue:{increase_day} ${increase}')
print(f'Greatest Decrease in Revenue:{decrease_day} ${decrease}')

#Create and print to text file
fh = open('budget.txt', 'w')

fh.write('Financial Analysis\n')
fh.write('------------------------------\n')
fh.write(f'Total Months:{tot_months}\n')
fh.write(f'Total Profit/Losses: ${tot_prof_loss}\n')
fh.write(f'Average Profit/Loss Change: ${average}\n')
fh.write(f'Greatest Increase in Revenue:{increase_day} ${increase}\n')
fh.write(f'Greatest Decrease in Revenue:{decrease_day} ${decrease}')

fh.close()