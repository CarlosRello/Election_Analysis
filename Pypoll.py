# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
election_results = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
election_summary = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(election_results) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)