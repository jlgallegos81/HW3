#import module
import os
import csv

#Set Variables
candidates = []
unique_candidate = []
votes = []
votes_percentage = []
count = 0

#Filepath
election_data = os.path.join("Resources","Resources", "election_data.csv")

# Open the csv
with open(election_data, newline="") as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")
	csv_header = next(csvreader)
	for row in csvreader:
		count = count +1
		candidates.append(row[2])
	for x in set (candidates):
		unique_candidate.append(x)
		y = candidates.count(x)
		votes.append(y)
		z = round((y/count)*100)
		votes_percentage.append(z)
   
	winning_votes = max(votes)
	winner = unique_candidate[votes.index(winning_votes)]

# Print the results
print("Drum roll please.........")
print("--------------------------------------------")
print("Total Votes: " + str(count))
print("--------------------------------------------")
for i in range(len(unique_candidate)):
			print(unique_candidate[i] + ": " + str(votes_percentage[i]) +"% (" + str(votes[i]) + ")")
print("--------------------------------------------")
print("Winning Candidate is: " + str(winner))
print("--------------------------------------------")


# Create the text file
with open("PyPoll.txt", "w") as output:
	output.write("Results are in!\n")
	output.write("Drum roll please..............!\n")
	output.write("--------------------------------------------\n")
	output.write("Total Votes: " + str(count) + "\n")
	output.write("--------------------------------------------\n")
	for i in range(len(unique_candidate)):
			print(unique_candidate[i] + ": " + str(votes_percentage[i]) +"% (" + str(votes[i]) + ")")
	output.write("--------------------------------------------\n")
	output.write("Winning Candidate is: " + str(winner) + "\n")
	output.write("--------------------------------------------\n")
