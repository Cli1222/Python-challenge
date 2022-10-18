import csv
import csv 
import os
from re import T

csvpath = os.path.join('Resources', 'budget_data.csv')

total_months = 0 
total_profit_loss = 0
changes_profit_loss = 0
totalchanges = 0
Greatest_increase=''
Greatest_increase_value = 0
Greatest_Decrease_value = 0
Greatest_Decrease = ''



with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile)

    csv_header = next(csvreader)

    for line in csvreader:
        if csvreader.line_num == 2:
            lastmonth = int(line[1])

        total_months = total_months + 1
        total_profit_loss = total_profit_loss + int(line[1])
        #changes = currentmonth - lastmonth
        change = int(line[1]) -lastmonth
        totalchanges = totalchanges + change

        lastmonth = int(line[1])
        if change > Greatest_increase_value:
            Greatest_increase_value = change
            Greatest_increase = line[0]
            
        if change< Greatest_Decrease_value:
            Greatest_Decrease_value = change
            Greatest_Decrease = line[0]





changes_profit_loss = totalchanges / (total_months - 1)




print("Financial Analysis")
print("--------------------------")
print(f'Total Months: {total_months}')
print(f'Total: ${total_profit_loss}')
print(f'Average change: ${changes_profit_loss:.2f}')
print(f'Greatest Increase In Profits: {Greatest_increase} ({Greatest_increase_value})')
print(f'Greatest Decrease In Profits: {Greatest_Decrease} ({Greatest_Decrease_value})')


