#import modules
import os
import csv
#reading csv
csvpath = os.path.join('.', 'Resources', 'budget_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
#loop through rows in each column, store Data in months_list, Profit/Losses in total_list    
    months_list = []
    total_list = []
    for row in csvreader:
        months_list.append(row[0])
        total_list.append(row[1])
#removed headers from each list
months_list.pop(0)
total_list.pop(0) 

#count how many months, turn profits/losses into integers and add up the list
months = len(months_list)
total = sum(int(t) for t in total_list)

#convert total_list from "string" into integer with a loop
for j in range(0, len(total_list)):
    total_list[j] = int(total_list[j])

#create a new change_list for the monthly change in profits/losses, using two new lists that edit total_list
change_list = []
total_list1 = [0] + total_list
total_list2 = total_list
total_list2.append(0)
#zip the two new total_lists, loop through the difference and store in change_list
zip_obj = zip(total_list1, total_list2)
for total_list1, total_list2 in zip_obj:
    change_list.append(total_list2-total_list1)
#fix change_list by dropping last and first elements
change_list.pop()
change_list.pop(0)

#store the average of the changes
average_change = sum(change_list)/len(change_list)
#store greatest increase and decrease in amount
increase = max(change_list)
decrease = min(change_list)
#loop through lists and store corresponding date
for k in range(0, len(change_list)):
    if change_list[k] == increase:
        increase_month = months_list[k+1]
    elif change_list[k] == decrease:
        decrease_month = months_list[k+1]

#print analysis to the terminal
print("Financial Analysis")
print("------------------------------")
print(f"Total Months: {months}")
print(f"Total: ${total}")
print("Average Change: $" + str(round(average_change, 2)))
print("Greatest Increase in Profits: " + increase_month + " ($" + str(increase) + ")")
print("Greatest Decrease in Profits: " + decrease_month + " ($" + str(decrease) + ")")

#export text file with results
file_finance = open(r"analysis\Financial_Analysis.txt","w+")
file_finance.write("Financial Analysis" + "\n")
file_finance.write("------------------------------" + "\n")
file_finance.write(f"Total Months: {months}" + "\n")
file_finance.write(f"Total: ${total}" + "\n")
file_finance.write("Average Change: $" + str(round(average_change, 2)) + "\n")
file_finance.write("Greatest Increase in Profits: " + increase_month + " ($" + str(increase) + ")" + "\n")
file_finance.write("Greatest Decrease in Profits: " + decrease_month + " ($" + str(decrease) + ")" + "\n")
file_finance.close()