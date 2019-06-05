import os
import csv
import numpy as np 

#Get the file
path = os.path.join('Resources', 'election_data.csv')

#declare Variables
voter_ID = []
candidates = []
winner_votes = 0


#Open file to read
with open(path,'r', newline='') as file:
    reader = csv.reader(file, delimiter=',')
    print(reader)
    header = next(reader)
    print(f"CSV Header: {header}")

    for row in reader:
        voter_ID.append(row[0])
        total_votes = len(voter_ID)
        candidates.append(row[2])
    unique_candidates = np.unique(candidates)

#Print Summary on console and write to output.txt file
file1 =  os.path.join('Resources', 'output.txt')
with open(file1, 'w') as text:
    print("")

    text.write("Election Results \n")
    print("Election Results")

    text.write("----------------------------\n") 
    print("----------------------------") 

    text.write(F"Total Votes: {total_votes} \n")     
    print(F"Total Votes: {total_votes}")

    text.write("---------------------------- \n")
    print("----------------------------")

    for i in range(0,len(unique_candidates)):
        candidate_Name = unique_candidates[i]
        candidate_votes = candidates.count(candidate_Name) 
        if candidate_votes > winner_votes:
            winner_votes = candidate_votes
            winner = candidate_Name
        percent_votes = (candidate_votes/total_votes) * 100

        text.write(F"{candidate_Name} : {'{:.3f}'.format(percent_votes)}% ({candidate_votes}) \n")
        print(F"{candidate_Name} : {'{:.3f}'.format(percent_votes)}% ({candidate_votes})")

    text.write("----------------------------\n")
    print("----------------------------")

    text.write(F"Winner: {winner} \n")
    print(F"Winner: {winner}")

    text.write("----------------------------\n")
    print("----------------------------")
