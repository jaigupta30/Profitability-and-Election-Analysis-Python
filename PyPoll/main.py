#imports
import csv
import os

csv_path = os.path.join ("Resources", "election_data.csv")
with open (csv_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
 # Lists

    ballot_id = []
    county = []
    candidate = []

    # Storing data in Lists
    #print(csvreader)
    for row in csvreader:
        ballot_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

    # Calculating Total Votes - 1
    total_votes = len(ballot_id) 
    #print(total_votes)

 # Number of particiapnts - 2
    candidate_row = set(candidate)
    #print(candidate_row)

    # Total Number of votes of each candidate - 4
    candidate1 = 0 # Raymon Anthony Doane
    candidate2 = 0 # Diana DeGette
    candidate3 = 0 # Charles Casper Stockham


    candidate_dictionary = {}
    percentage_dictionary = {}

    # Set the initial dictionary with unique candidate names
    for i in candidate_row:
        candidate_dictionary[i] = 0
        percentage_dictionary[i] = 0
    # Count the unique candidate names each time they appeared in candidate array
    for i in candidate:
        candidate_dictionary[i] += 1
    #print((candidate_dictionary))

    # Percentage of Vote of each candidate - 3
    for i in candidate_dictionary:
        percentage_dictionary[i] = round(((candidate_dictionary[i] / total_votes) * 100), 3)
    #print(percentage_dictionary)

    # Most voted candidate - 5
    print(candidate_dictionary)
    most_voted = max(zip(candidate_dictionary.values(), candidate_dictionary.keys()))[1]
    print(most_voted)

#Outputs

print (f"Election Results")
print (f"")
print (f"----------------------")
print (f"")
print(total_votes)
print (f"")
print (f"----------------------")
print ("")
#print (f"{dd}")
print (f"")
#print (f"Winner: {dd}")
print (f"")
print (f"----------------------")

 #text file output
txt_file = os.path.join("Analysis", "PyPoll_Analysis.txt")

with open(txt_file, mode= 'w') as file:   
    file.write(
    f"Election Results\n"
    f"\n"
    f"----------------------\n"
    f"\n"
    f"Total Votes: {total_votes}\n"
    f"\n"
    f"----------------------\n"
    f"\n"
    f"Charles Casper Stockham{percentage_dictionary['Charles Casper Stockham']} {candidate_dictionary['Charles Casper Stockham']}\n"
    f"Diana DeGette{percentage_dictionary['Diana DeGette']} {candidate_dictionary['Diana DeGette']}\n"
    f"Raymon Anthony Doane{percentage_dictionary['Raymon Anthony Doane']} {candidate_dictionary['Raymon Anthony Doane']}\n"
    f"\n"
    f"----------------------\n"
    f"\n"
    f"Winner: {most_voted}\n"
    f"\n"
    f"----------------------\n")