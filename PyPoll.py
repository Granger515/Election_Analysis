# Add our dependencies

import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

#Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#1. Initialize a total vote counter variable
total_votes = 0

#Create a list of possible candidates
candidate_options = []

#create a dictonary to hold candidate names and number of votes
candidate_votes ={}

# Winning Candidate and Winning Count Tracker variables are initialized here
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: perform analysis.
    file_reader = csv.reader(election_data)

    # Skip the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:

        #2. Add to the total vote count (total_votes+=1 is the same as total_votes = total_votes +1)
        total_votes+=1

        # Print the candidate name from each row (this is assigning the value in the location to the candidate_name variable)
        candidate_name = row[2]

        #Sets up a condition to check and see if a value is not already present in a list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list. (adding the candidate_name to the candidate_options list)
            candidate_options.append(candidate_name)

            #Add a vote to that candidate's count.
            candidate_votes[candidate_name] = 0

        #Add a vote for the candidate total count
        candidate_votes[candidate_name] += 1

    # Save the results to our text file.
    with open(file_to_save, "w") as txt_file:
        # Print the final vote count to the terminal.
        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n")
       
        print(election_results, end="")
        # Save the final vote count to the text file.
        txt_file.write(election_results)

        # Determine the percentage of votes for each candidate by looping through the counts.

        # 1. Iterate through the candidate list.
        for candidate_name in candidate_votes:

            # 2. Retrieve vote count of a candidate.
            votes = candidate_votes[candidate_name]

            # 3. Calculate the percentage of votes.
            vote_percentage = float(votes) / float(total_votes) * 100

            #Creates a variable for each candidates results then prints it
            candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

            # Print each candidate, their voter count, and percentage to the terminal.
            print(candidate_results)

            #  Save the candidate results to our text file.
            txt_file.write(candidate_results)

            #Print out each candidate's name, vote count, and percentage of
            # votes to the terminal.
            #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

            # Determine winning vote count and candidate
            # 1. Determine if the votes are greater than the winning count.
            if (votes > winning_count) and (vote_percentage > winning_percentage):

                # 2. If true then set winning_count = votes and winning_percent =
                # vote_percentage.
                winning_count = votes
                winning_percentage = vote_percentage

                # 3. Set the winning_candidate equal to the candidate's name.
                winning_candidate = candidate_name


    #Prints winning candidate with summary
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)


#######################################################################

# Read and print the header row. - Old Code (QA)
 #headers = next(file_reader)
#print(headers)

 # 4. Print the candidate name and percentage of votes. Old Code (QA)
#print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")

# Print the candidate vote dictionary. Old Code (QA)
#print(candidate_votes)

#Print the candidate list - Old Code (QA) prints the values in the candidate_list list
#print(candidate_options)

#3. Print the total votes - Old code (QA) printing total votes
#print(total_votes)

    #Old code (QA) to print each row of the CSV file
        #print(row)

    ## Old code (QA) to 
    # Print the file object.
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