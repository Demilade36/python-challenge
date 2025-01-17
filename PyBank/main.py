# Dependencies
import csv
import os

# Set path for file
budget_data=  os.path.join("PyBank","Resources", "budget_data.csv")  # Input file path
budget_analysis = os.path.join("PyBank","analysis", "budget_analysis.txt")  # Output file path


# Define variables to track the financial data
total_months = 0
total_net = 0
prior_profit_loss = None
changes = []
dates = []


# Open the CSV using the UTF-8 encoding
with open(budget_data, encoding='UTF-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=",")

     # Skip the header row
    header = next(reader)

     #Process each row of data
    for row in reader:
        # Assign values to variables with descriptive names
        date = row[0]     
        profit_loss = int(row[1])    

        #To sum total the months and the Net profit/loss total 
        total_months = total_months + 1
        total_net = total_net + profit_loss

        # Generate changes and track dates
        if prior_profit_loss is not None:
            net_change = profit_loss - prior_profit_loss
            changes.append(net_change)
            dates.append(date)

        prior_profit_loss = profit_loss

# Generate the greatest increase in profits (month and amount)
greatest_increase = max(changes)

# Generate the greatest decrease in losses (month and amount)
greatest_decrease = min(changes)

# Generate Output summary
average_change = sum(changes) / len(changes)
greatest_increase_date = dates[changes.index(greatest_increase)]
greatest_decrease_date = dates[changes.index(greatest_decrease)]

# Print the output
output = (
     "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n"
    )

# Print the output
print(output)

# Write the results to a text file
with open(budget_analysis, "w") as txt_file:
   txt_file.write(output)