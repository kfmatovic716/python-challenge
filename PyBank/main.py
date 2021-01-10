import pathlib
import csv
from statistics import mean

#creates a file path for the csv file
csvpath = pathlib.Path("Resources", "budget_data.csv")

#empty lists to fill later
months = []         #elements taken from csv file
profit_losses =[]   #elements taken from csv file
PL_change = []      #created as new list, elements taken from calculation 

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
     # Read the header row first 
    csvheader = next(csvreader)
    print(f"CSV Header: {csvheader}")

     # Read each row of Date and Profit/Losses after the header
    for row in csvreader:
        
        months.append(row[0])
        profit_losses.append(int(row[1]))
    
#Converts strings in profit_losses list to integers & append to PL_integers list
#Use this list for calculation of average change in P/L
print(profit_losses)

#Months
total_months = len(months)  #Calculates total number of months in data    

#Amount
total_amount = sum(profit_losses)     #Calculates sum

#P/L Change
'''HUNTER ~ Set the first month elememt (NOT SURE IF CORRECT to do this way)'''
PL_change.append(profit_losses[0]) 

#Loop for appending the rest of the elements in 
for x,y in zip(profit_losses[0:], profit_losses[1:]):
    PL_change.append(y-x)

'''HUNTER ~ tried converting to list comprehension but getting a syntax error
 i think it's because PL_change is not completely empty?
#elements = zip(profit_losses[0:], profit_losses[1:]
#PL_change = [(y-x) for x,y in elements]    '''

#To check if the elements appended above are correct
print(PL_change) 

#Calculating average of changes in P/L (use PL_change list)
'''HUNTER ~ are we supposed to match the average change from the README file  of the hw, which is $-2315.12.
I got 7803.47!  I calculated manually in Excel and my answer is correct. Did I misunderstand something? Why is the number in README 
is different?'''

Average = mean(PL_change)

#List conversion to dictionary to combine months and P/L changes
months_PLchg = dict(zip(months, PL_change)) 
#print(months_PLchg)

#Calculations of min and max
highest_profit = max(months_PLchg.keys(), key=(lambda k: months_PLchg[k]))
lowest_profit = min(months_PLchg.keys(), key=(lambda k: months_PLchg[k]))


#Summary
print("Financial Analysis")
print("-------------------")
print(f'Total Months: {total_months}') 
print(f"Total Net Profit/Losses:  ${total_amount}") 
print(f"Average Change in Profit/Losses: {Average}")  
print(f"Greatest Increase in Profits: {highest_profit}, {months_PLchg[highest_profit]}")
print(f"Greatest Decrease in Profits: {lowest_profit}, {months_PLchg[lowest_profit]}")




#DRAFT(delete later)
#another option using function to calc avg
#def average(amounts):
#     total = sum(amounts)
#     count = len(amounts)
#     return total / count

# Average = average(PL_change)
    
   
   


