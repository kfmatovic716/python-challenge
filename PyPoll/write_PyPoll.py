# Dependencies
import pathlib
import csv

# Specify the file to write to
PyPoll_output = pathlib.Path("Analysis/PyPoll_Analysis.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(file=PyPoll_output, mode='w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['Candidate Name', 'Total Vote Count', 'Percentage Vote'])
        
    # Write candidate results on the following 4 rows
    csvwriter.writerow(['Khan', 2218231, 63])
    csvwriter.writerow(['Correy', 704200, 20])
    csvwriter.writerow(['Li', 492940, 14])
    csvwriter.writerow(["O'Tooley", 105630, 3])

    #Start new column header for total votes & the result in the following row
    csvwriter.writerow(['Total Votes'])
    csvwriter.writerow([3521001])

    #Start new column header for the winner & the result in the following row
    csvwriter.writerow(['Winning Candidate'])
    csvwriter.writerow(['Khan'])

