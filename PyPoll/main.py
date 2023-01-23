import os
import csv
from statistics import mode

election_csvpath = os.path.join('Resources', 'election_data.csv')

candidate_list = []

with open(election_csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    csv_header = next(csvreader)

    for row in csvreader:
        candidate_list.append(row[2])

    def candidates_count(candidate):
        final_count = candidate_list.count(candidate)
        return final_count

    candidate1 = "Charles Casper Stockham"
    candidate2 = "Diana DeGette"
    candidate3 = "Raymon Anthony Doane"

    def candidates_per(candidate):
        total = len(candidate_list)
        candidate_per = round((candidates_count(candidate) / total) * 100, 3)
        return candidate_per
    
    print("Election Results")
    print("-------------------------")
    print(f"Total votes: {len(candidate_list)}")
    print("-------------------------")
    print(f"{candidate1}: {candidates_per(candidate1)}% ({candidates_count(candidate1)})")
    print(f"{candidate2}: {candidates_per(candidate2)}% ({candidates_count(candidate2)})")
    print(f"{candidate3}: {candidates_per(candidate3)}% ({candidates_count(candidate3)})")
    print("-------------------------")
    print(f"Winner: {mode(candidate_list)}")
    print("-------------------------")

    output_path = os.path.join("analysis", "results_PyPoll.txt")

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