#imported two libraries and two specific functions (from other libraries) I'm using.
import os
import csv
from math import fsum
from statistics import mean

#specified the file path associated with the financial data (no .. was necessary
#because in this case there's no need to level up one directory).
findata_csv = os.path.join("Resources", "budget_data.csv")

#created two lists that will hold all the dates and profits/loses. 
date_list = []
ProfitLoses_list = []

#read the CSV file with the financial data.
with open(findata_csv) as csvfile:
    #specified the delimiter and a variable that holds the contents.
    csvreader = csv.reader(csvfile, delimiter= ",")
    #read the header row.
    csv_header = next(csvreader) 

    #read each row of data after the header and added the elements of the first column (dates)
    #and second column (profits and loses) of the CSV file to my Python lists.
    for row in csvreader:
        date_list.append(row[0])
        ProfitLoses_list.append(int(row[1]))
    
    #calculated the total amount of "Profit/Losses" over the entire period.
    net_total = fsum(ProfitLoses_list)
    
    #created a new list to hold the changes in "Profit/Losses" over the entire period
    #and calculated the average of those changes.
    diff_list = [ProfitLoses_list[i + 1] - ProfitLoses_list[i] for i in range(len(ProfitLoses_list)-1)]
    ave_change = round(mean(diff_list), 2)
    
    #calculated the greatest increase and decrease in profilts over the entire period.
    max_index = diff_list.index(max(diff_list))
    min_index = diff_list.index(min(diff_list))

    #printed the financial analysis to the terminal.
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {len(date_list)}") #calculated the total number of months in the dataset.
    print(f"Total: $ {int(net_total)}") #casted net_total to get rid of the decimals.
    print(f"Average Change: ${ave_change}")
    print(f"Greatest Increase in Profits: {date_list[(max_index + 1)]} (${max(diff_list)})") #included the date.
    print(f"Greatest Decrease in Profits: {date_list[(min_index + 1)]} (${min(diff_list)})") #included the date.

    #specified a new file path to export the financial analysis results (no .. was necessary
    #because in this case there's no need to level up one directory).
    output_path = os.path.join("analysis", "results_PyBank.txt")

    #exported the same analysis to a TXT file.
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