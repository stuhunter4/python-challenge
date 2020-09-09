#import modules
import os
import csv

#reading csv and skipping headers
csvpath = os.path.join('.', 'Resources', 'election_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
#loop throw csv, store relevant columns into new lists
    voter_list = []
    candidate_list = []
    for row in csvreader:
        voter_list.append(row[0])
        candidate_list.append(row[2])

#count how many voter IDs in first column, store as total_votes
total_votes = len(voter_list)

#create new list for candidates, looking for unique candidate values
#loop through candidate_list, check if element exists in candidates_name or not
candidates_name = []
for candidate in candidate_list:
    if candidate not in candidates_name:
        candidates_name.append(candidate)

#create new list, counting total number of votes per candidate in cadidates_name list
candidate_count = []
for x in range(0, len(candidates_name)):
    candidate_counter = candidate_list.count(candidates_name[x])
    candidate_count.append(candidate_counter)

#create new list, calculate and store percentage of votes per candidate
percentage_list = []
for y in range(0, len(candidate_count)):
    percent_votes = ((candidate_count[y]/total_votes)*100)
    percentage_list.append(percent_votes)
#conditional to find the highest number of votes and store the corresponding candidate
    if candidate_count[y] == max(candidate_count):
        winner = candidates_name[y]

#print analysis to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
#loop to print candidates and their results from respective lists
for z in range(0, len(percentage_list)):
    print(str(candidates_name[z]) + ": " + format(percentage_list[z], '.3f') + "% (" + str(candidate_count[z]) + ")")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

#export text file with results
file_election = open(r"analysis\Election_Results.txt","w+")
file_election.write("Election Results" + "\n")
file_election.write("-------------------------" + "\n")
file_election.write(f"Total Votes: {total_votes}" + "\n")
file_election.write("-------------------------" + "\n")
for z in range(0, len(percentage_list)):
    file_election.write(str(candidates_name[z]) + ": " + format(percentage_list[z], '.3f') + "% (" + str(candidate_count[z]) + ")" + "\n")
file_election.write("-------------------------" + "\n")
file_election.write(f"Winner: {winner}" + "\n")
file_election.write("-------------------------" + "\n")
file_election.close()