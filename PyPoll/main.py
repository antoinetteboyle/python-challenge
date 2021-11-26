## PyPoll

![Vote Counting](Images/Vote_counting.png)

* In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.

* You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:

  * The total number of votes cast

  * A complete list of candidates who received votes

  * The percentage of votes each candidate won

  * The total number of votes each candidate won

  * The winner of the election based on popular vote.

* As an example, your analysis should look similar to the one below:

  ```text
  Election Results
  -------------------------
  Total Votes: 3521001
  -------------------------
  Khan: 63.000% (2218231)
  Correy: 20.000% (704200)
  Li: 14.000% (492940)
  O'Tooley: 3.000% (105630)
  -------------------------
  Winner: Khan
  -------------------------
  ```

* In addition, your final script should both print the analysis to the terminal and export a text file with the results.

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



  avg_change = sumdiff/(monthcount-1) # mean(change)
  avg_change = round(avg_change,2)  
  
  greatest_increase = max(change)
  
  greatest_decrease = min(change)
  
  indexi = (int(change.index(greatest_increase))) + 1
  
  increase_month = monthlist[int(indexi)]
  indexj = (int(change.index(greatest_decrease))) + 1
  
  decrease_month = monthlist[int(indexj)]

print("PyBank")
print("FINANCIAL ANALYSIS")
print("----------------------------------")             
print(f"Total months: {monthcount}")
print(f"Total Profit and Loss: ${TotProfitLoss}")
print(f"Average Change in Profit and Loss: ${avg_change}")
print(f"Greatest Increase in Profits: {increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})")

# save the output file path
output_file = os.path.join("pybank_final.txt")

# open the output file as variable 
with open(output_file, 'w') as f:
    f.write('readme')






tupleszip = zip(monthlist, pllist)  # Then zip these lists together into a single tuple.

# save the output file path
output_file = os.path.join("pybank_final.csv")

# open the output file as variable 
with open(output_file, "w") as datafile:

    writer = csv.writer(datafile) # Initialize variable/object for csv.writer
# create a header row   
    writer.writerow(["Month", "Profit and Loss", "Change"]) #new titles
# write the zipped object to the csv or just type out the detailed row lists for each heading above
    writer.writerows(tupleszip) 
def avg_change()
        diff = diff.append.row[1]
        # using list comprehension generate successive difference list
        res = [diff[i + 1] - diff[i] for i in range(len(diff)-1)]
  
        # printing result
        print ("The computed successive difference list is : " + str(res))