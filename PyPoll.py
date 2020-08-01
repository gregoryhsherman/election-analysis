import csv
import os

#Assign load variable
file_to_load = os.path.join("Resources", "election_results.csv")
#Assign save variable
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Open election results and read
with open(file_to_load) as election_data:
    file_reader= csv.reader(election_data)
    
    #Print header row
    headers = next(file_reader)
    print(headers)
    