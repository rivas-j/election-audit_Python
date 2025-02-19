import csv
import os

# Add a variable to load a file from a path
file_to_load = "data/election_results.csv"

# Add a variable to save the file to a path
file_to_save = "election_analysis.txt"

# Initialize a total vote counter
total_votes = 0

# Candidate Options and candidate votes
candidate_options = []
candidate_votes = {}

# Create a county list and county votes dictionary
county_list = []
county_votes = {}

# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Track the largest county and county voter turnout
largest_county = ""
highest_county_voter_turnout = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file: 
        # - add to the total vote count
        # - get the candidate name for each row
        # - extract the county name from each row
    for row in reader:

        total_votes = total_votes + 1
        candidate_name = row[2]
        county_name = row[1]

        # If the candidate does not match any existing candidate add it to
        # the candidate list and begin tracking that candidate's voter count
        if candidate_name not in candidate_options:

            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] += 1

        # If county does not match any existing county in the county list,
        # Add the existing county to the list of counties and begin tracking the county's vote count
        if county_name not in county_list:

            county_list.append(county_name)
            county_votes[county_name] = 0

        # Add a vote to that county's vote count
        county_votes[county_name] += 1


# Save the results to output text file
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)

    # For loop to get the county from the county dictionary
    for county_name in county_votes:
        
        # Retrieve the county vote count
        county_turnout = county_votes.get(county_name)

        # Calculate the percentage of votes for the county
        county_vote_percentage = float(county_turnout) / float(total_votes) * 100

        # Print the county results to the terminal
        county_results = (f"{county_name}: {county_vote_percentage:.1f}% ({county_turnout:,})\n")
        print(county_results)
        
        # Save the county votes to a text file
        txt_file.write(county_results)
        
        # Write an if statement to determine the winning county and get its vote count
        if (county_turnout > highest_county_voter_turnout):
            highest_county_voter_turnout = county_turnout
            largest_county = county_name
    # Print the county with the largest turnout to the terminal
    largest_county_result = (
        f"-------------------------\n"    
        f"Largest County Turnout: {largest_county}\n"
        f"-------------------------\n"    
    )
    
    print(largest_county_result)

    # Save the county with the largest turnout to a text file
    txt_file.write(largest_county_result)

    # Save the final candidate vote count to the text file
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal
        print(candidate_results)
        
        # Save the candidate results to our text file
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
