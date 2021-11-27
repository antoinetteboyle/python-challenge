#Python challenge PyBank

import os
import csv

# variable for path to collect data from the Resources folder
pybank_budget_data_csv = os.path.join('Resources', 'budget_data.csv')

# Create lists per header/column to store/assign your column values to variables   
monthcount = 0
TotProfitLoss = 0
monthlist = []
pllist =[]

avg_change = 0
greatest_increase = 0
increase_month = 0
greatest_decrease = 0
decrease_month = 0
sumdiff = 0
diff = 0
change = []  


# Read in the CSV file
with open(pybank_budget_data_csv, 'r') as csvfile:
  csvreader = csv.reader(csvfile)
  # will skip the header row
  header = next(csvreader)

  # Loop through the data
  for row in csvreader:

     monthlist.append(row[0])   #create a month list
     monthcount = monthcount +1  # keep count of the months

     pllist.append(row[1])   # create a profit and loss list

     TotProfitLoss =  TotProfitLoss + int(row[1])  #calculated the total profit and loss


  for x1, x2 in zip(pllist[:-1], pllist[1:]):
        try:
          diff = (int(x2) - int(x1))   # cells b3-b2
          sumdiff = sumdiff + diff 
        except ZeroDivisionError:
          diff = None
        change.append(diff)

  avg_change = sumdiff/(monthcount-1) # calculate mean(change)
  avg_change = round(avg_change,2)  

  greatest_increase = max(change)   # calculate max

  greatest_decrease = min(change)   # calculate min
  
  indexi = (int(change.index(greatest_increase))) + 1 # calculate max index and find month
  increase_month = monthlist[int(indexi)]
  
  indexj = (int(change.index(greatest_decrease))) + 1  # calculate min index and find month
  decrease_month = monthlist[int(indexj)]

# Print to screen
print("PyBank")
print("FINANCIAL ANALYSIS")
print("----------------------------------")             
print(f"Total months: {monthcount}")
print(f"Total Profit and Loss: ${TotProfitLoss}")
print(f"Average Change in Profit and Loss: ${avg_change}")
print(f"Greatest Increase in Profits: {increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})")

# save the output file path
write_file = os.path.join("analysis","pybank_final.txt")

# open the output file as variable and print to text file 
with open(write_file, 'w') as f:
  f.write('PyBank')
  f.write('\n')
  f.write('FINANCIAL ANALYSIS')
  f.write('\n')
  f.write('----------------------------------')
  f.write('\n')
  f.write(f"Total months: {monthcount}")
  f.write('\n')
  f.write(f"Total Profit and Loss: ${TotProfitLoss}")
  f.write('\n')
  f.write(f"Average Change in Profit and Loss: ${avg_change}")
  f.write('\n')
  f.write(f"Greatest Increase in Profits: {increase_month} (${greatest_increase})")
  f.write('\n')
  f.write(f"Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})")
