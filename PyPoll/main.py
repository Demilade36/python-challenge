# Import necessary modules
import csv
import os

# Files to load and output
election_data = os.path.join("PyPoll", "Resources", "election_data.csv")  # Input file path
election_analysis = os.path.join("PyPoll", "analysis", "election_analysis.txt")  # Output file path

# Variables to track the election data
total_votes = 0  # Track the total number of votes cast
candidate_votes = {}  # Dictionary to store votes for each candidate
results = []  # List to store candidate details

# Winning Candidate and Winning Count Tracker
winner = None
winner_votes = 0

# Open the CSV using UTF-8 encoding
with open(election_data, encoding='UTF-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:
        total_votes += 1
        candidate = row[2]

        # Count votes for each candidate
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

# Calculate the percentage of votes and determine the winner
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    results.append((candidate, votes, percentage))

    if votes > winner_votes:
        winner = candidate
        winner_votes = votes

# Generate the output string
output = (
    "Election Results\n"
    "-------------------------\n"
    f"Total Votes: {total_votes}\n"
    "-------------------------\n"
)

for candidate, votes, percentage in results:
    output += f"{candidate}: {percentage:.3f}% ({votes})\n"

output += (
    "-------------------------\n"
    f"Winner: {winner}\n"
    "-------------------------\n"
)

# Print the output
print(output)