#Python Challenge PyPoll:

import os
import csv

# variable for path to collect data from the Resources folder
pypoll_data_csv = os.path.join('Resources', 'election_data.csv')

# Create lists per header/column to store/assign your column values to variables   
totvotes = 0
candidatelist = []
    
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
  perc = 0
  print("PyPoll")
  print("Election results: ")
  print("-----------------------------")   
  print("Total votes: ",totvotes) 
  print("-----------------------------")

# calculate the amount of votes per candidate and print to screen
  for x in candidatelist:
    d.setdefault(x,0)
    d[x] += 1
  for x, count in d.items():  # iterate through candidate vote list using the dictionary
    perc = round((count/totvotes*100),1)     # calculate percentage of total votes
    print("{}:   {}%    ({})". format(x,perc,count))

  winner = max(d, key=d.get)       # find the winner based on max votes
  print("-----------------------------")
  print("The winner is: ",winner)
  print("-----------------------------")
 
# save the output file path
output_file = os.path.join("analysis","pypoll_final.txt")

# open the output file as variable 
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
  d = {}
  perc = 0
  for x in candidatelist: # calculate the amount of votes per candidate and print to file
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