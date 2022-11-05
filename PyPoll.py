# Add our dependencies

import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

#Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: perform analysis.
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)

        # Print each row in the CSV file.
    # for row in file_reader:
    #     print(row)

    ## Print the file object.
    # print(election_data)


##############################################################################

#The data we need to retrieve


# #How to impost a CSV file from a direct path (exact location of file known)

# import csv

# file_to_load = 'Resources/election_results.csv'

# # Open the election results and read the file
# with open(file_to_load) as election_data:

#     # To do: perform analysis.
#     print(election_data)

# #How to import a CSV file from an indirect path (file folder known but specific path not known) 

# How to write a file

# Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# # Use the open statement to open the file as a text file.
# with open(file_to_save, "w") as txt_file:

    # Write some data to the file. (each individually)
    #  txt_file.write("Arapahoe ")
    #  txt_file.write("Denver ")
    #  txt_file.write("Jefferson")

    # Write some data to the file. (all at once)
    #txt_file.write("Arapahoe, Denver, Jefferson")

    # Write some data to the file. (all at once - each one on a new line)
    # txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")

    #1. Total number of votes cast
    #2 A complete list of candidates who received votes
    #3 the percentage of votes each candidate won
    #4 the winner of the election based on popular vote