import os
import csv
from math import fsum
from statistics import mean

findata_csv = os.path.join("Resources", "budget_data.csv")

date_list = []
ProfitLoses_list = []

with open(findata_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")
    csv_header = next(csvreader) 

    for row in csvreader:
        date_list.append(row[0])
        ProfitLoses_list.append(int(row[1]))
    
    net_total = fsum(ProfitLoses_list)
    
    diff_list = [ProfitLoses_list[i + 1] - ProfitLoses_list[i] for i in range(len(ProfitLoses_list)-1)]
    ave_change = round(mean(diff_list),2)
    diff_list.index(max(diff_list))
    
    max_index = diff_list.index(max(diff_list))
    min_index = diff_list.index(min(diff_list))

    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {len(date_list)}")
    print(f"Total: $ {int(net_total)}")
    print(f"Average Change: ${ave_change}")
    print(f"Greatest Increase in Profits: {date_list[(max_index + 1)]} (${max(diff_list)})")
    print(f"Greatest Decrease in Profits: {date_list[(min_index + 1)]} (${min(diff_list)})")

    output_path = os.path.join("analysis", "results_PyBank.txt")

    with open(output_path, 'w') as txtfile:
        txtfile.write("Financial Analysis")
        txtfile.write("\n")
        txtfile.write("----------------------------")
        txtfile.write("\n")
        txtfile.write(f"Total Months: {len(date_list)}")
        txtfile.write("\n")
        txtfile.write(f"Total: $ {int(net_total)}")
        txtfile.write("\n")
        txtfile.write(f"Average Change: ${ave_change}")
        txtfile.write("\n")
        txtfile.write(f"Greatest Increase in Profits: {date_list[(max_index + 1)]} (${max(diff_list)})")
        txtfile.write("\n")
        txtfile.write(f"Greatest Decrease in Profits: {date_list[(min_index + 1)]} (${min(diff_list)})")