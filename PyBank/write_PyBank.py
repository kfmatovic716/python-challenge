# Dependencies
import pathlib
import csv

# Specify the file to write to
PyBank_output = pathlib.Path("Analysis/PyBank_Analysis.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(file=PyBank_output, mode='w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['Total Months', 'Total Net P&L', 'Average Change in P&L', 'Greatest Increase in Profit', 'Greatest Decrease in Profit'])
        
    # Write the second row for actual results
    csvwriter.writerow([86, 38382578, 7803, 'Feb-2012 1926159', 'Sep-2013 -2196167'])
