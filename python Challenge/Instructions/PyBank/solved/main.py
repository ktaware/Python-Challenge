import os
import csv

main_csv = os.path.join('..','Resources','budget_data.csv')

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
        rowCount = rowCount + 1
        print(rowCount+1)
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
    print("Financial Analysis")
    print("----------------------------------------------")
    print(f"Total Months : {rowCount}")
    print(f"Profit Losses total : ${totalProfitLoss}")
    print(f"Average Change : ${round(avgChange,2)}")
    print(f"Greatest Increase in Profits: {IncreaseDate} (${greatestIncreaseInProfits}) ")
    print(f"Greatest Decrease in Profits: {decreaseDate} (${greatestDecreaseInProfits}) ")
    
    
    
    
        
    

   
   





