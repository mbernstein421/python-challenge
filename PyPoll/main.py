import os, csv

infile = os.path.join(".", "Resources", "election_data.csv")
outfile = os.path.join(".", "analysis", "election_results.txt")

total_count = 0
candidates = {}

with open(infile) as csv_file:
    csvreader = csv.reader(csv_file)
    header=next(csvreader)
#The total number of votes cast
    for row in csvreader:
        total_count += 1
#A complete list of candidates who received votes        
        candidate = row[2]
        candidates[candidate] = candidates.get(candidate, 0) +1

#The percentage of votes each candidate won

 
with open(outfile, "w") as txt_file:

    output = (
        f"Election Results\n"
        f"----------------------------\n"
        f"Total Votes: {total_count}\n"
        f"Total Candidates {candidates}"
    )

    print(output)
    txt_file.write(output)





#The total number of votes cast

#A complete list of candidates who received votes

#The percentage of votes each candidate won

#The total number of votes each candidate won

#The winner of the election based on popular vote