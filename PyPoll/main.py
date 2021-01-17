import pathlib
import csv

#creates a file path for the csv file
csvpath = pathlib.Path("Resources", "election_data.csv")

#Empty lists to be filled later with election data from csv file
voters = []
county = []
candidate = []
candidates_summary = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
     # Read the header row first 
    csvheader = next(csvreader)

     # Read each row of Voter ID, County and Candidate after the header
    for row in csvreader:
        
        voters.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

#Creates a new list of candidates without duplicates
candidates_summary = sorted(list(set(candidate)))

#Creates a list of total counts for each candidate
votecounts = [candidate.count(cand) for cand in candidates_summary]
sorted_counts = sorted(votecounts)

#Calculates total votes, same results as len(voters)
totalvotes = sum(votecounts)  

#Function to calculate % of votes for each candidate
def percentage(each_count, total):
    pct = round((each_count / total) * 100, 4)
    return pct

#Put percentage votes in a list
Pct_Votes = [percentage(cand, totalvotes) for cand in votecounts]

#Convert to dictionary to use in determining winner
candidate_pctvotes = dict(zip(candidates_summary, Pct_Votes)) 
sorted_candpctvotes = dict(sorted(candidate_pctvotes.items(), key=lambda item:item[1], reverse=True))

# Determines the winner
winner =  max(candidate_pctvotes.keys(), key=(lambda k: candidate_pctvotes[k]))

#output
print("ELECTION RESULTS")
print("--------------------------------")
print(f"Total Votes:  {totalvotes}")
print("--------------------------------")
print(f"{candidates_summary[1]}: {sorted_candpctvotes[candidates_summary[1]]} % ({sorted_counts[3]})")
print(f"{candidates_summary[0]}: {sorted_candpctvotes[candidates_summary[0]]} % ({sorted_counts[2]})")
print(f"{candidates_summary[2]}: {sorted_candpctvotes[candidates_summary[2]]} % ({sorted_counts[1]})")
print(f"{candidates_summary[3]}: {sorted_candpctvotes[candidates_summary[3]]} % ({sorted_counts[0]})")
print("--------------------------------")
print(f"WINNER: {winner}")


# Specify the file to write to
PyPoll_output = pathlib.Path("Analysis/PyPoll_Analysis.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(file=PyPoll_output, mode='w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['Candidate Name', 'Percentage Vote', 'Total Vote Count'])
        
    # Write candidate results on the following 4 rows
    csvwriter.writerow([candidates_summary[1], sorted_candpctvotes[candidates_summary[1]], sorted_counts[3]])
    csvwriter.writerow([candidates_summary[0], sorted_candpctvotes[candidates_summary[0]], sorted_counts[2]])
    csvwriter.writerow([candidates_summary[2], sorted_candpctvotes[candidates_summary[2]], sorted_counts[1]])
    csvwriter.writerow([candidates_summary[3], sorted_candpctvotes[candidates_summary[3]], sorted_counts[0]])

    #Start new column header for total votes & the result in the following row
    csvwriter.writerow(['Total Votes'])
    csvwriter.writerow([totalvotes])

    #Start new column header for the winner & the result in the following row
    csvwriter.writerow(['Winning Candidate'])
    csvwriter.writerow([winner])
