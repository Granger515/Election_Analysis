# Election_Analysis

## Project Overview

A colorado Board of Elections employee has given me the following tasks to complete in the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2 Get a complete list of candidates who received votes.
3. Calculate the total number votes each candidate received.
4 Calculate the percentage of votes each candidate received.
5 Determine the winner of the election based on popular vote.

## Resources
-Data source: election_results.csv
-Software: Python 3.7.6

## Summary

The analysis of the election shows that:
-There were 369,711 votes cast in the election.
-The candidates were:
  -Charles Casper Stockham
  -Diana DeGette
  -Raymon Anthony Doane
The candidate results were:
  -Charles Casper Stockham received 23.0% of the vote and 85,213 votes.
  -Diana DeGette received 73.8% of the vote and 272,892 votes.
  -Raymon Anthony Doane received 3.1% of the vote and 11,606 votes.
The winner of the election was:
  -Diana DeGette who received 73.8% of the vote and 272,892 votes.
  
## Challenge Overview
Using the same data as provided earlier provide a breakdown county data as follows:

1. Identify the counties in the election.
2. Calculate the number of votes cast in each county.
3. Calculate the percentage of total votes cast in each county.
4. Calculate the county with the largest number of votes cast.

## Challenge Summary

The county level analysis of the votes cast shows that:
-The counties were:
  -Jefferson
  -Denver
  -Arapahoe
-The number of votes cast in each county were as follows:
  -Jefferson 38,855
  -Denver 306,055
  -Arapahoe 24,801
-The percentage of total votes in this election broken down by county were as follows:
  -Jefferson 10.5%
  -Denver 82.8%
  -Arapahoe 6.7%
 -The county with the largest number of voters to turn out was:
  -Denver
 
##Proposal of Alternative use of Scripts

The most obvious use of this script in future elections would be in alternative statewide elections such as disticts for the House of Representatives, Senate, Governor races. This would require no modification of the script other than changes to the read and write files script. This could either be done manually on a case-by-case or the use of inputs to collect values used for the file location, the input file, and the text file to write the results to. These values could be stored in variables and the variables used to direct the analysis to the proper data input and output.

Another use of the script would be in tracking voter registrant participation. This would require more extensive modifications to the script and more data for analyses. The extra data would be included in CSV file listing each county and the number of registered voters. This could be added into the analyses and a percentage of total voters that participated out of registered voters could be calculated. Over time this could suggest counties where more in-person voting facilities were needed. 

