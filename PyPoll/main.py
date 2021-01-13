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
    #print(f"CSV Header: {csvheader}") 

     # Read each row of Voter ID, County and Candidate after the header
    for row in csvreader:
        
        voters.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

#To get list of candidates, sort the candidate list first
sorted_candidatelist = sorted(candidate)

#Creates a new list of candidates without the duplicates
candidates_summary = sorted(list(set(sorted_candidatelist)))
#print(candidates_summary)

#Creates a list of total counts for each candidate
votecounts = [candidate.count(cand) for cand in candidates_summary]
sorted_counts = sorted(votecounts)
#print(sorted_counts)

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
#print(sorted_candpctvotes)

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
print(f"WINNER: {winner}, {candidate_pctvotes[winner]} %")

