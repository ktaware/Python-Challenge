# Create a Python script that analyzes the PyBank records to calculate each of the following:
# -->>  The total number of months included in the dataset
# -->>  The net total amount of "Profit/Losses" over the entire period
# -->>  The average of the changes in "Profit/Losses" over the entire period
# -->>  The greatest increase in profits (date and amount) over the entire period
# -->>  The greatest decrease in losses (date and amount) over the entire period
# -->>  Print the analysis to the terminal and export a text file with the results


#add our dependencies.
import os
import csv

#Assign a variable to laod a file from a path
main_csv = os.path.join('..','Resources','budget_data.csv')

# -->>  Export a text file with the results
fName = os.path.join("..","analysis","budget_data.txt")
f = open(fName, "w")

with open(main_csv,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    rowCount = 0
    totalProfitLoss = 0
    totalChange = 0
    previousProfitLoss = 0
    greatestIncreaseInProfits = 0
    greatestDecreaseInProfits = 0
    
    for row in csvreader:
        # Count of months
        rowCount = rowCount + 1
        currentProfitLoss = int(row[1])
        
        totalProfitLoss = (currentProfitLoss) + totalProfitLoss
        if rowCount==1:
            previousProfitLoss = currentProfitLoss
            continue
        currentChange = (currentProfitLoss - previousProfitLoss)
        totalChange = totalChange + currentChange
        previousProfitLoss = currentProfitLoss
        
        if (currentChange > greatestIncreaseInProfits):
            IncreaseDate = row[0]
            #print(IncreaseDate)
            greatestIncreaseInProfits= currentChange 
        elif(currentChange < greatestDecreaseInProfits):
            decreaseDate = row[0]
            #print(decreaseDate)
            greatestDecreaseInProfits = currentChange
            
    avgChange = totalChange / (rowCount-1)
    # -->>  Print the analysis to the terminal
    f.write("Financial Analysis\n")
    f.write("----------------------------------------------\n")
    f.write(f"Total Months : {rowCount}\n")
    f.write(f"Profit Losses total : ${totalProfitLoss}\n")
    f.write(f"Average Change : ${round(avgChange,2)}\n")
    f.write(f"Greatest Increase in Profits: {IncreaseDate} (${greatestIncreaseInProfits})\n")
    f.write(f"Greatest Decrease in Profits: {decreaseDate} (${greatestDecreaseInProfits})\n")
    
    
    
    
        
    

   
   





