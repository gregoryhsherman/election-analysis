# The Data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote. 


# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initialize a total vote counter.
total_votes = 0
# Candidate options and candidate votes.
candidate_options = []
candidate_votes = {}
# Create a list for counties.
counties_names = []
# Create a dictionary 
# where the county is the key and the votes 
# cast for each county in the election are the values.
counties_votes = {}
# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0
#Create an empty string that will hold the county name that had the largest turnout.
Largest_county_turnout = ""
Largest_county_count = 0
Largest_county_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Get the candidate name from each row.
        candidate_name = row[2]
        # If the candidate does not match any existing candidate, add the
        # the candidate list.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
        # Challenge
        # Declare a variable that represents the number of votes that a county received. 
        # Hint: Inside a for loop, add an if statement to check if the county name has already been recorded. 
        # If not, add it to the list of county names.
        county_name = row[1]
        if  county_name not in counties_names:
            # Add the county name to the county list.
            counties_names.append(county_name)
            # And begin tracking that county's voter count.
            counties_votes[county_name] = 0
        # Add a vote to that county's count.
        counties_votes[county_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal + County Votes Summary.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
        f"\nCounty Votes:\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)
 
# Inside the with open() function where you are outputting the file, do the following:
# Create three if statements to print out the voter turnout results similar to the results shown above.
# Add the results to the output file.
# Print the results to the command line.
    for county in counties_votes:
        # Retrieve vote count and percentage for each county.
        vote = counties_votes[county]
        votes_percentage = float(vote) / float(total_votes) * 100
        county_results = (f"{county}: {votes_percentage:.1f}% ({vote:,})\n")


        # Print each county's voter count and percentage to the terminal.
        print(county_results)
        #  Save the county results to our text file.
        txt_file.write(county_results)
        # Determine largest county vote count, largest county percentage, and largest county turnout.
        if (vote > Largest_county_count) and (votes_percentage >Largest_county_percentage):
            Largest_county_count = vote
            Largest_bounty_turnout = county
            Largest_county_percentage = votes_percentage
    # Print the largest county's results to the terminal.
    Largest_county_summary = (
        f"\n-------------------------\n"
        f"Largest County Turnout: {Largest_bounty_turnout}\n"
        f"-------------------------\n")
    print(Largest_county_summary)
    # Save the largest county's results to the text file.
    txt_file.write(Largest_county_summary)
 
 
    for candidate in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")



        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage
    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)






         


