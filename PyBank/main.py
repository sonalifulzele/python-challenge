
import os
import csv

#Get the CSV File
path = os.path.join('Resources', 'budget_data.csv')
#print(path)

#Open the CSV file to read
with open(path, newline='') as file:
    reader = csv.reader(file, delimiter=',')
    #print(reader)
    header = next(reader)
    #print(f"CSV Header: {header}")
    
    month_counter = 0
    total_amount = 0
    avg_change = 0
    change_profit_loss = [] 
    #total_change_profit_loss = []
    prev_profit_loss = 0
    curr_profit_loss = 0
    period = []
    for row in reader:
        #print(row)
        month_counter += 1
        total_amount += int(row[1])
        period.append(row[0])
        if month_counter == 1 :
            prev_profit_loss = int(row[1]) 
            change_profit_loss.append(0.0)
            continue
        else:
            curr_profit_loss = int(row[1])
            change_profit_loss.append(curr_profit_loss - prev_profit_loss) 
        prev_profit_loss = curr_profit_loss
    avg_change = sum(change_profit_loss)/(month_counter-1)
    greatest_incr_profit = max(change_profit_loss)
    greatest_decr_profit = min(change_profit_loss)
    idx_maximum = change_profit_loss.index(max(change_profit_loss))
    idx_minimum = change_profit_loss.index(min(change_profit_loss))
    print("")
    print("Financial Analysis")  
    print("--------------------------------------------------")     
    print(F"Total Months: {month_counter}")
    print(F"Total: {total_amount}")
    print(F"Average Change: {'{:.2f}'.format(avg_change) }")
    print(F"Greatest Increase in Profits: {period[idx_maximum]} (${greatest_incr_profit})")
    print(F"Greatest Increase in Profits: {period[idx_minimum]} (${greatest_decr_profit})")









        
