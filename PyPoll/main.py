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
    #print(f"CSV Header: {csvheader}") --delete later

     # Read each row of Voter ID, County and Candidate after the header
    for row in csvreader:
        
        voters.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

#To get list of candidates, sort the candidate list first
sorted_candidatelist = sorted(candidate)

#Loop through the sorted list & add candidates that are not in the summary yet
for name in sorted_candidatelist:
    if name not in candidates_summary:
        candidates_summary.append(name)
'''HUNTER, I was just trying to convert the above for loop to a list comprehension (line 36)but for some reason 
it's not working, any thoughts? Did I do it wrong? I know you said this is not advisable at this stage but i was just curious..
 candidates_summary = [name for name in sorted_candidatelist if name not in candidates_summary] '''

#print(candidates_summary) --delete later

#Calculate total counts for each vote
Candidate1 = candidate.count(candidates_summary[0])
Candidate2 = candidate.count(candidates_summary[1])
Candidate3 = candidate.count(candidates_summary[2])
Candidate4 = candidate.count(candidates_summary[3])

votecounts = [Candidate1, Candidate2, Candidate3, Candidate4]
totalvotes = sum(votecounts)  #same result when you get len(voters)

'''HUNTER, below is another OPTION to calculate Pct, i know this looks redundant but it's less line of code than
what I've actually used. Which one is better to do? With the function or this 4 lines of stinky program that you call.
I thought to use function just to show that I know how to create/use a function since that might be part of grading criteria.
 Pct_Vote1 = round((votecounts[0] / totalvotes) * 100, 2)
 Pct_Vote2 = round((votecounts[1] / totalvotes) * 100, 2)
 Pct_Vote3 = round((votecounts[2] / totalvotes) * 100, 2)
 Pct_Vote4 = round((votecounts[3] / totalvotes) * 100, 2)'''

#Function to calculate % of votes for each candidate
def percentage(each_count, total):
    pct = round((each_count / total) * 100, 4)
    return pct

Pct_Vote1 = percentage(Candidate1, totalvotes)
Pct_Vote2 = percentage(Candidate2, totalvotes)
Pct_Vote3 = percentage(Candidate3, totalvotes)
Pct_Vote4 = percentage(Candidate4, totalvotes)

#Convert to dictionary to use in determining winner
Pct_Votes = [Pct_Vote1, Pct_Vote2, Pct_Vote3, Pct_Vote4]
candidate_pctvotes = dict(zip(candidates_summary, Pct_Votes)) 
 
winner =  max(candidate_pctvotes.keys(), key=(lambda k: candidate_pctvotes[k]))

print("ELECTION RESULTS")
print("--------------------------------")
print(f"Total Votes:  {totalvotes}")
print("--------------------------------")
print(f"{candidates_summary[1]}: {Pct_Vote2} % ({Candidate2})")
print(f"{candidates_summary[0]}: {Pct_Vote1} % ({Candidate1})")
print(f"{candidates_summary[2]}: {Pct_Vote3} % ({Candidate3})")
print(f"{candidates_summary[3]}: {Pct_Vote4} % ({Candidate4})")
print("--------------------------------")
print(f"WINNER: {winner}, {candidate_pctvotes[winner]} %")

