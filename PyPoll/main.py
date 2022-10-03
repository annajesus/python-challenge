# import modules
import os
import csv

# locate csv file 
election_data_csv = os.path.join('Resources', 'election_data.csv')

# Set variables
# Count the total number of votes each candidate has
total_votes = 0
# Store the name of the candidates
candidate_list = []
# Store the number of votes each candidate has
number_votes = []
# Store the % of total votes for each candidate 
vote_percentage = []

# Open csv file to read
with open(election_data_csv,newline="") as election_data:
    csv_reader = csv.reader(election_data,delimiter=",") 

    # Skip the header 
    header = next(csv_reader)     

    # Loop thru each row in the csv
    for row in csv_reader:
        # The total number of votes cast
        total_votes = total_votes + 1

        # The total number of votes cast / A complete list of candidates who received votes
        # If candidate not on the list, add candidate name to the list, and store a vote to candidate name
        # If candidate on the list, add a vote to candidate name
        if row[2] not in candidate_list:
            # loop thru rows and add candidate to list 
            candidate_list.append(row[2])
            # assign index
            cand_index = candidate_list.index(row[2])
            # loop thru and add the number of votes to list
            number_votes.append(1)
        else:
            cand_index = candidate_list.index(row[2])
            # add votes to the candidate_list by finding the matching index and adding 1 to its value
            number_votes[cand_index] += 1 
        
        # The percentage of votes each candidate won
        for votes in number_votes:
            # calculate the total percent of votes for each candidate
            percent = (votes/total_votes) * 100
            # format results "%f=floating point numbers" 
            percent = "%f" % percent
            # loop thru and add the % of total votes to list
            vote_percentage.append(percent)
        
        

        # The winner of the election based on popular vote.
        winner = max(number_votes)
        winner_index = number_votes.index(winner)
        winner = candidate_list[winner_index]


# Print results
print('Election Results')
print('*-*-*-*-*-*-*-*-*-*-*-*-*-*')
print(f'Total Votes: {str(total_votes)}')
print('*-*-*-*-*-*-*-*-*-*-*-*-*-*')
for c in range(len(candidate_list)):
    print(f"{candidate_list[c]}: {str(percent[c])} ({str(number_votes[c])})")
print('*-*-*-*-*-*-*-*-*-*-*-*-*-*')
print(f'Winner: {winner}')
print('*-*-*-*-*-*-*-*-*-*-*-*-*-*')

#Export and print results to text file
file = open('PyPoll_Analysis_Results', 'w')
file.write('Election Results''\n')
file.write('*-*-*-*-*-*-*-*-*-*-*-*-*-*''\n')
file.write(('Total Votes: ' + str(total_votes)))
file.write('\n')
file.write('*-*-*-*-*-*-*-*-*-*-*-*-*-*''\n')
for c in range(len(candidate_list)):
    file.write(f"{candidate_list[c]}: {str(percent[c])} ({str(number_votes[c])})")
    file.write('\n')
file.write('*-*-*-*-*-*-*-*-*-*-*-*-*-*''\n')
file.write(f'Winner: {winner}' '\n')



