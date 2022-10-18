import csv
import csv 
import os
from re import T

csvpath = 'election_data.csv'

total_vote = 0 
received_vote = 0
percentage_of_vote = 0
total_number_of_vote = 0
popular_vote_winner= 0
Winner = ""
candidate ={}
candidate_list =[]

winnder = ""

maxVotes = 0

i = 1

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
   

    csv_header = next(csvreader)

    for line in csvreader:
        total_vote = total_vote +1
        candidate_name = line[2]
        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)
            candidate[candidate_name]=0
        candidate[candidate_name]=candidate[candidate_name]+1

    for individual in candidate:
        if maxVotes < candidate[individual]:
            maxVotes = candidate[individual]
    

        

   
        



print("Election Results")
print("--------------------------")
print(f'Total Votes: {total_vote}')
print("--------------------------")
for key,value in candidate.items():
    print(f'{key}:{value/total_vote*100:.3f}% ({value})')
#print(f'Charles Casper Stockham: {candidate}')
#print(f'Diana DeGette: {percentage_of_vote}')
#print(f'Raymon Anthony Doane: {total_number_of_vote}')
print("--------------------------")
print(f'Winner: {maxVotes}')
print("--------------------------")

