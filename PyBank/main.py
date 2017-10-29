'''

## Option 1: PyBank

![Revenue](Images/revenue-per-lead.jpg)

Python script for analyzing the financial records of a company. Two sets of revenue data:

(`budget_data_1.csv` and `budget_data_2.csv`). 

Each dataset is composed of two columns: `Date` and `Revenue`. 

(The company has rather lax standards for accounting so the records are simple.)

The task is to create a Python script that analyzes the records to calculate each of the following:

* The total number of months included in the dataset

* The total amount of revenue gained over the entire period

* The average change in revenue between months over the entire period

* The greatest increase in revenue (date and amount) over the entire period

* The greatest decrease in revenue (date and amount) over the entire period

As an example, your analysis should look similar to the one below:

'''




# import the modules

import os 
import csv

# file path 

file_path = os.path.join('raw_data', 'budget_data_1.csv')



revenue = []
months = []

# open the file 
with open(file_path, newline=None) as csvfile:

    # read the file
    csv_reader = csv.reader(csvfile, delimiter = ',')

    # skip the first row / header
    next(csvfile, None)

    # loop for appending for revenue and months
    for row in csv_reader:
        revenue.append(int(row[1]))
        months.append(row[0])

# find number of total months and sum of the revenue 
months_lenght = len(revenue)
revenue_total = sum(revenue)


# determine incraese and decrease for entire period in revenue 
first_value = revenue[0]
change_between = []

for k in revenue:
    difference = k - first_value
    change_between.append(difference)
    first_value = k 

# set up the max and min value between months 
max_value = [a for a, b in enumerate(change_between) if b == (max(change_between))][0]
min_value = [a for a, b in enumerate(change_between) if b == (min(change_between))][0]

# find the average change in revenue 
average_change_revenue = ((sum(change_between))/(len(change_between)-1))

# find the greatest increase/decrease in month and change 
greatest_increase_month = months[max_value]
greatest_increase_change = max(change_between)

greatest_decrease_month = months[min_value]
greatest_decrease_change = min(change_between)

# print all the needed information 

print('Financial Analysis: ')

print('...........................................')

print('Total Months: ' + str(months_lenght))
print('Total Revenue: $' + str(revenue_total))
print('Average Revenue Change: $' + str(average_change_revenue))
print('Greatest Increase in Revenue: ' + greatest_increase_month +" $"+ str(greatest_increase_change))
print('Greatest Decrease in Revenue: ' + greatest_decrease_month +" $"+ str(greatest_decrease_change))

print('...........................................')