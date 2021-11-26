#PyPoll


#   ```text
#   Election Results
#   -------------------------
#   Total Votes: 3521001
#   -------------------------
#   Khan: 63.000% (2218231)
#   Correy: 20.000% (704200)
#   Li: 14.000% (492940)
#   O'Tooley: 3.000% (105630)
#   -------------------------
#   Winner: Khan
#   -------------------------
#   ```

# * In addition, your final script should both print the analysis to the terminal and export a text file with the results.

import os
import csv

# variable for path to collect data from the Resources folder
pypoll_data_csv = os.path.join('Resources', 'election_data.csv')

# Create lists per header/column to store/assign your column values to variables   
totvotes = 0
candidatelist = []
uniqueset = ()
    
# Read in the CSV file
with open(pypoll_data_csv, 'r') as csvfile:
  csvreader = csv.reader(csvfile)
  # will skip the header row
  header = next(csvreader)

  # Loop through the data
  for row in csvreader:
    
    candidatelist.append(row[2])   # create full candidate vote list
    totvotes = totvotes +1       # keep count of the votes
   
  d = {}
  candi = ""
  perc = 0
  print("PyPoll")
  print("Election results: ")
  print("-----------------------------")   
  print("Total votes: ",totvotes) 
  print("-----------------------------")


  for x in candidatelist:
    d.setdefault(x,0)
    d[x] += 1
  for x, count in d.items():
    perc = round((count/totvotes*100),1)
    print("{}:   {}%    ({})". format(x,perc,count))

  winner = max(d, key=d.get)
  print("-----------------------------")
  print("The winner is: ",winner)
  print("-----------------------------")
 
# # save the output file path
output_file = os.path.join("analysis","pypoll_final.txt")

# # open the output file as variable 
with open(output_file, 'w') as f:

  f.write('PyPoll')
  f.write('\n')
  f.write('ELECTION RESULTS:')
  f.write('\n')
  f.write('------------------------------')
  f.write('\n')
  f.write(f"Total votes: {totvotes}")
  f.write('\n')
  f.write('------------------------------')
  f.write('\n')
  for x in candidatelist:
    d.setdefault(x,0)
    d[x] += 1
  for x, count in d.items():
    perc = round((count/totvotes*100),1)
    f.write("{}:   {}%    ({})". format(x,perc,count))
    f.write('\n')
  winner = max(d, key=d.get)
  f.write("-----------------------------")
  f.write('\n')
  f.write(f"The winner is: " + winner)
  f.write('\n')
  f.write("-----------------------------")