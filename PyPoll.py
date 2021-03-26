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

# Initializes a total vote counter
total_votes = 0

#Creates empty list for candidates
candidate_options = []
# Declares empty dictionary tracking votes for candidates
candidate_votes = {}

# Winning candidate and winning vote count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Reads the header row
    headers = next(file_reader)

    for row in file_reader:
        # Adds votes in each row in the CSV file to the total number of votes
        total_votes += 1
        #Adds candidate names to candidate list only once
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            # Begins tracking candidate vote counts
            candidate_votes[candidate_name] = 0
        # Adds vote to candidate's count
        candidate_votes[candidate_name] += 1    

# Saves results to text file
with open(file_to_save, "w") as txt_file:

    # Prints final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Saves final vote count to text file
    txt_file.write(election_results)

    # Calculates vote percentage for each candidate in candidate_votes dictionary
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = (float(votes) / float(total_votes)) * 100
        # Prints each candidate's name, their voter count, and their vote percentage to the terminal
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        # Saves candidate results to text file
        txt_file.write(candidate_results)

        # Determines winning vote count and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    # Prints out information for winning candidate
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Saves winning candidate information to text file
    txt_file.write(winning_candidate_summary)