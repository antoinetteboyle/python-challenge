## PyBank

""" 
![Revenue](Images/revenue-per-lead.png)

* In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. You will give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). The dataset is composed of two columns: `Date` and `Profit/Losses`. (Thankfully, your company has rather lax standards for accounting so the records are simple.)

* Your task is to create a Python script that analyzes the records to calculate each of the following:

  * The total number of months included in the dataset

  * The net total amount of "Profit/Losses" over the entire period

  * Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes

  * The greatest increase in profits (date and amount) over the entire period

  * The greatest decrease in profits (date and amount) over the entire period

* As an example, your analysis should look similar to the one below:

  ```text
  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $38382578
  Average  Change: $-2315.12
  Greatest Increase in Profits: Feb-2012 ($1926159)
  Greatest Decrease in Profits: Sep-2013 ($-2196167)
  ```

* In addition, your final script should both print the analysis to the terminal and export a text file with the results.
 """

import os
import csv
# variable for path to collect data from the Resources folder
pybank_budget_data_csv = os.path.join('..', 'Resources', 'budget_data.csv')

# Create lists per header/column to store/assign your column values to variables   
monthcount = 0
TotProfitLoss = 0
monthlist = []
profitlosslist =[]
diff = []
avg_change = 0
greatest_increase = 0
increase_month = 0
greatest_decrease = 0
decrease_month = 0
   
print("PyBank")
print("FINANCIAL ANALYSIS")
print("----------------------------------")
    
# Read in the CSV file
with open(pybank_budget_data_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    # will skip the header row
    header = next(csvreader)

    # Loop through the data
    for row in csvreader:
        
        monthlist = monthlist.append.row[0]
        monthcount = len(monthlist)

        profitlosslist = profitlosslist.append.row[1]
        TotProfitLoss = sum(profitlosslist) #calculated the total profit and loss
        averageprofitloss = TotProfitLoss/monthcount
        
        # using list comprehension generate successive difference list
        diff = [profitlosslist[i + 1] - profitlosslist[i] for i in range(len(profitlosslist)-1)]
        greatest_increase = max(diff)
        greatest_decrease = min(diff)
        avg_change =  TotProfitLoss/monthcount   # mean(diff)

        # printing result
        #print ("The computed successive difference list is : " + str(res))

        if greatest_increase == row[1]:
          increase_month.append(row[0])
            
        if greatest_decrease == row[1]:    
          decrease_month.append(row[0])
             
        print(f"Total months: {monthcount})")
        print(f"Total Profit and Loss: {TotProfitLoss}")
        print(f"Average Change in Profit and Loss{avg_change}")
        print(f"Greatest Increase in Profits: {increase_month} ({greatest_increase})")
        print(f"Greatest Decrease in Profits: {decrease_month} ({greatest_decrease})")



