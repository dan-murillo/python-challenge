#imported two libraries and one specific function I'm using.
import os
import csv
from statistics import mode

#specified the file path associated with the election data (no .. was necessary
#because in this case there's no need to level up one directory).
election_csvpath = os.path.join('Resources', 'election_data.csv')

#created a list that will hold all the ballots choices ('Candidate' column). 
candidate_list = []

#read the CSV file with the election data.
with open(election_csvpath) as csvfile:
    #specified the delimiter and a variable that holds the contents.
    csvreader = csv.reader(csvfile, delimiter= ',')
    #read the header row.
    csv_header = next(csvreader)

    #read each row of data after the header and added the elements of
    #the third column (ballots choices) of the CSV file to my Python list.
    for row in csvreader:
        candidate_list.append(row[2])

    #defined a function that counts the votes of any candidate.
    def candidates_count(candidate):
        final_count = candidate_list.count(candidate)
        return final_count

    #defined the names of the election's candidates to pass them as arguments
    #of the functions I created.
    candidate1 = "Charles Casper Stockham"
    candidate2 = "Diana DeGette"
    candidate3 = "Raymon Anthony Doane"

    #defined a function that calculates the percentage of votes of any candidate
    #and uses the previous function that counts the votes of any candidate.
    def candidates_per(candidate):
        total = len(candidate_list)
        candidate_per = round((candidates_count(candidate) / total) * 100, 3)
        return candidate_per
    
    #printed the analysis to the terminal by calling the functions I created.
    print("Election Results")
    print("-------------------------")
    print(f"Total votes: {len(candidate_list)}")
    print("-------------------------")
    print(f"{candidate1}: {candidates_per(candidate1)}% ({candidates_count(candidate1)})")
    print(f"{candidate2}: {candidates_per(candidate2)}% ({candidates_count(candidate2)})")
    print(f"{candidate3}: {candidates_per(candidate3)}% ({candidates_count(candidate3)})")
    print("-------------------------")
    print(f"Winner: {mode(candidate_list)}") #found the winner by using the 'mode' function of the 'statistics' module.
    print("-------------------------")

    #specified a new file path to export the analysis results (no .. was necessary
    #because in this case there's no need to level up one directory).
    output_path = os.path.join("analysis", "results_PyPoll.txt")

    #exported the analysis to a TXT file.
    with open(output_path, 'w') as txtfile:
        txtfile.write("Election Results")
        txtfile.write("\n")
        txtfile.write("-------------------------")
        txtfile.write("\n")
        txtfile.write(f"Total votes: {len(candidate_list)}")
        txtfile.write("\n")
        txtfile.write("-------------------------")
        txtfile.write("\n")
        txtfile.write(f"{candidate1}: {candidates_per(candidate1)}% ({candidates_count(candidate1)})")
        txtfile.write("\n")
        txtfile.write(f"{candidate2}: {candidates_per(candidate2)}% ({candidates_count(candidate2)})")
        txtfile.write("\n")
        txtfile.write(f"{candidate3}: {candidates_per(candidate3)}% ({candidates_count(candidate3)})")
        txtfile.write("\n")
        txtfile.write("-------------------------")
        txtfile.write("\n")
        txtfile.write(f"Winner: {mode(candidate_list)}")
        txtfile.write("\n")
        txtfile.write("-------------------------")