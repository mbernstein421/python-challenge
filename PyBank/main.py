import os,csv

infile = os.path.join(".", "Resources", "budget_data.csv")
outfile = os.path.join(".", "analysis", "budget_analysis.txt")

total_month = 0
total_profit = 0
previous_profit = 0
total_change = 0
largest_amount = 0
largest_amount_date = ""
smallest_amount = 0
smallest_amount_date = ""


with open(infile) as csv_file:
    csvreader = csv.reader(csv_file)
    header = next(csvreader)

    for row in csvreader:
       # The total number of months included in the dataset
        total_month += 1
       # The net total amount of "Profit/Losses" over the entire period 
        profit = int(row[1])
       # The changes in "Profit/Losses" over the entire period, and then the average of those changes
        total_profit += profit

        if previous_profit != 0:
            change = profit - previous_profit
            total_change += change

        previous_profit = profit
       # The greatest increase in profits (date and amount) over the entire period 
        if profit > largest_amount:
            largest_amount = profit
            largest_amount_date = row[0]
       # The greatest decrease in profits (date and amount) over the entire period
        if profit < smallest_amount:
            smallest_amount = profit
            smallest_amount_date = row[0]
      
          


average_change = total_change / (total_month - 1)    
        


with open(outfile,"w") as txt_file:

    output = (
        f"Financial Analysis\n"
        f"----------------------------\n"
        f"Total Months: {total_month}\n"
        f"Total Profits/losses: {total_profit}\n"
        f"Average Change: {average_change}\n"
        f"Greatest Increase in Profit: {largest_amount_date} {largest_amount}\n"
        f"Greatest Increase in Profit: {smallest_amount_date} {smallest_amount}\n"
     
    )
    print(output)
    txt_file.write(output)


# The total number of months included in the dataset

# The net total amount of "Profit/Losses" over the entire period

# The changes in "Profit/Losses" over the entire period, and then the average of those changes

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in profits (date and amount) over the entire period