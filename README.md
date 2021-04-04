# Colorado Election Audit

## Project Overview
Assist Colorado Board of Elections employee with conducting an election audit using results from the U.S. congressional precinct in Colorado. Following pieces of information were requested:
- total number of votes
- number of votes for each candidate
- percentage of votes for each candidate
- identification of winner of election

## Resources
- data is from election_results.csv
- Software: Python 3.7.6, Visual Studio code, 1.54.3

## Results
Ultimately, the analysis revealed that:
- There were a total of 369,711 votes cast in the election
- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The results for each candidate were:
    - Charles Casper Stockham: 23.0% of the vote (85,213 votes received)
    - Diana DeGette: 73.8% of the vote (272,892 votes received)
    - Raymon Anthony Doane: 3.1% of the vote (11,606 votes received)
- The winner was Diana DeGette, who received 73.8% of the vote (i.e., 272,892 out of 369,711 votes)

## Challenge Election Audit Overview

### Purpose
For this challenge, the python code that was used to find the election result information requested by the Colorado Board of Elections in the Project Overview section above was updated to find, output, and record in the [election_analysis](https://github.com/HannaKim4673/Election_Analysis/blob/main/analysis/election_analysis.txt) text file 3 new pieces of information:
- each county's voter turnout
- the percentage of votes for each county
- identification of the county with the highest voter turnout

To clarify, the election data that was analyzed for this election audit came from the [election_results.csv](https://github.com/HannaKim4673/Election_Analysis/blob/main/Resources/election_results.csv) file.

## Challenge Election Audit Results
The election audit revealed the following pieces of information, which can also be seen in the Python code output image below:
- There were a total of 369,711 votes cast in the election
- The percentage of votes and voter turnout (i.e., number of votes) for each county was:
    -  Jefferson County: 10.5% of votes (38,855 votes)
    -  Denver County: 82.8% of votes (306,055 votes)
    -  Arapahoe County: 6.7% of votes (24,801 votes)
-  Denver County had the largest number of votes
- The results for each candidate were:
    - Charles Casper Stockham: 23.0% of the vote (85,213 votes received)
    - Diana DeGette: 73.8% of the vote (272,892 votes received)
    - Raymon Anthony Doane: 3.1% of the vote (11,606 votes received)
- The winner was Diana DeGette, who received 73.8% of the vote (i.e., 272,892 out of 369,711 votes)

![](https://github.com/HannaKim4673/Election_Analysis/blob/main/Election%20Audit%20Output.png)

## Challenge Election Audit Summary
In order to make this project's python code usable for any election, the following two changes can be made. The below line

![](https://github.com/HannaKim4673/Election_Analysis/blob/main/Original%20Code%201.png)

(which is used to load the file holding the colorado election data) can be changed to an a series of lines that includes input statements like this:

![](https://github.com/HannaKim4673/Election_Analysis/blob/main/Suggested%20Additions/Suggested%20Revision.png)

This way, the python code will be able to read in and load data for any election as opposed to being set to always analyze the Colorado election data file. Another change that can make the code usable for other elections would be to add the following highlighted lines of code:

![](https://github.com/HannaKim4673/Election_Analysis/blob/main/Suggested%20Additions/Suggested%20Addition%201.png)
![](https://github.com/HannaKim4673/Election_Analysis/blob/main/Suggested%20Additions/Suggested%20Addition%202.png)
![](https://github.com/HannaKim4673/Election_Analysis/blob/main/Suggested%20Additions/Suggested%20Addition%203.png)
![](https://github.com/HannaKim4673/Election_Analysis/blob/main/Suggested%20Additions/Suggested%20Addition%204.png)
![](https://github.com/HannaKim4673/Election_Analysis/blob/main/Suggested%20Additions/Suggested%20Addition%205.png)
![](https://github.com/HannaKim4673/Election_Analysis/blob/main/Suggested%20Additions/Suggested%20Addition%206.png)

By doing that, the code will be able to perform audits for national elections as well as state elections. In the end, the revised code should resemble the code in this [PyPoll Suggested Revisions.txt](https://github.com/HannaKim4673/Election_Analysis/blob/main/Suggested%20Additions/PyPoll%20Suggested%20Revision.txt) file.
