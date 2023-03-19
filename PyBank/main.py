#imports
import csv
import os


csv_path = os.path.join("Resources", "budget_data.csv")

def printFstring(message = '', data = ''):
    if (len(data) > 0):
        return f"{message} : ${data}\n"
    else:
        return f"{message}\n"
with open (csv_path,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)
    #print (csv_header)
   
    #variables
    date = []
    profit = []
    monthly_changes = []
    profit_change=[]

    profit_loss_change = []
  
    # Problems
    # 1: Total Number of months in data set
    # 2: Net total p/l over timeperiod
    # 3: Changes in p/l and average of those changes
    # 4: Greatest increase in profits over entire period
    # 5: Greatest decrease in profits over entrire period

    for row in csvreader:
      date.append(row[0])
      profit.append(int((row[1])))
        

    profittotal=sum(profit)
    for i in range(len(date) - 1):
        current_month = i
        next_month = i + 1
        profit_loss_change.append(profit[next_month] - profit[current_month])
    average_of_pl_changes = round((sum(profit_loss_change) / len(profit_loss_change)), 2)


    greatest_increase_profit = max(profit_loss_change)
    greatest_decrease_profit = min(profit_loss_change)
txt_file = os.path.join("Analysis", "PyBank_Analysis.txt")
with open(txt_file, mode= 'w') as file:
    file.write(printFstring('Financial Analysis'))
    file.write(printFstring('-----------------------------'))
    file.write(printFstring('Total Months', str(len(date))))
    file.write(printFstring('Total', str(profittotal)))
    file.write(printFstring('Average Change', str(average_of_pl_changes)))
    file.write(printFstring('Greatest Increase in Profit', str(greatest_increase_profit)))
    file.write(printFstring('Greatest Decrease in Profit', str(greatest_decrease_profit)))