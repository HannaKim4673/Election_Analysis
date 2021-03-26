# Data the needs to be retrieved:
# 1. Total number of votes cast
# 2. Complete list of candidates who received votes
# 3. Percentage of votes each candidate won
# 4. Total number of votes each candidate won
# 5. Winner of election based on popular vote

#Adds dependencies
import csv
import os
# Assigns variable for file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")
# Assigns a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Reads and prints the header row
    headers = next(file_reader)
    print(headers)



# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:
    
    # Write header
    txt_file.write("Counties in the Election\n")
    # Write dashed line
    txt_file.write("-------------------------\n") 
    # Write three counties to the file.
    txt_file.write("Arapahoe\nDenver\nJefferson")