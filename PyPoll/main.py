import os
import csv
from statistics import mode
from collections import Counter

election_csvpath = os.path.join('Resources', 'election_data.csv')

candidate_list = []

with open(election_csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    csv_header = next(csvreader)

    for row in csvreader:
        candidate_list.append(row[2])

    candidate1_count = candidate_list.count("Charles Casper Stockham")
    candidate2_count = candidate_list.count("Diana DeGette")
    candidate3_count = candidate_list.count("Raymon Anthony Doane")
    total = candidate1_count + candidate2_count + candidate3_count

    candidate1_per = round((candidate1_count / total) * 100, 3)
    candidate2_per = round((candidate2_count / total) * 100, 3)
    candidate3_per = round((candidate3_count / total) * 100, 3)

    print("Election Results")
    print("-------------------------")
    print(f"Total votes: {len(candidate_list)}")
    print("-------------------------")
    print(f"Charles Casper Stockham: {candidate1_per}% ({candidate1_count})")
    print(f"Diana DeGette: {candidate2_per}% ({candidate2_count})")
    print(f"Raymon Anthony Doane: {candidate3_per}% ({candidate3_count})")
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
        txtfile.write(f"Charles Casper Stockham: {candidate1_per}% ({candidate1_count})")
        txtfile.write("\n")
        txtfile.write(f"Diana DeGette: {candidate2_per}% ({candidate2_count})")
        txtfile.write("\n")
        txtfile.write(f"Raymon Anthony Doane: {candidate3_per}% ({candidate3_count})")
        txtfile.write("\n")
        txtfile.write("-------------------------")
        txtfile.write("\n")
        txtfile.write(f"Winner: {mode(candidate_list)}")
        txtfile.write("\n")
        txtfile.write("-------------------------")