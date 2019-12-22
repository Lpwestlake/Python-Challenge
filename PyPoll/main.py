import os
import csv 

# define read path (run from Python-Challenge folder)
csvpath = os.path.join("Pypoll", "Resources/election_data.csv")

# define write path for output (run from Python-Challenge folder)
output_path = os.path.join("PyPoll", "Output/PyPoll.txt")

# C:\Users\westl\Desktop\Python-Challenge\Python-Challenge\PyPoll\Resources\election_data.csv

with open(csvpath, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

   # designate header row
    csv_header = next(csv_reader)

# define dictionary
    results = {}

# define variables
    total_votes = 0

# create for loop
    for row in csv_reader:
    # calculate total vote count and create dictionary to use candidate name only once
    # counts votes for each candidate  
        total_votes = total_votes + 1
        if row[2] in results.keys():
            results[row[2]] = results[row[2]] + 1
        else:
            results[row[2]] = 1

# create lists for candidates, vote counts, and percentage
    candidates = []
    votes = []
    percent_vote = [] 

# takes the dictionary keys and values puts into the lists candidates and votes lists
    for key, value in results.items():
        candidates.append(key)
        votes.append(value)

# takes the number of votes and divides by total for each candidate to give percentage    
    for x in votes:
        percentage = round(x/total_votes*100,3)
        percent_vote.append(percentage)

# zips data to create new cleaned up list
    zip_data = list(zip(candidates,votes,percent_vote))

# loops through zipped data to get winner that has most votes
    for y in zip_data:
        if max(votes) == y[1]:
            winner = y[0]

  
# generate print statmeents
print("Election Results")
print("-------------------------")
print(f"Total Votes: {str(total_votes)}")
print("-------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(percent_vote[i])}% ({str(votes[i])})")
print("-------------------------")
print(f"Winner: {str(winner)}")
print("-------------------------")

# open the file using "write" mode
with open(output_path, 'w') as txtfile:

# rite the print statements including '\n' to dictate end of line
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {str(total_votes)}\n")
    txtfile.write("-------------------------\n")
    for i in range(len(candidates)):   
        txtfile.write(f"{candidates[i]}: {str(percent_vote[i])}% ({str(votes[i])})\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {str(winner)}\n")
    txtfile.write("-------------------------\n")