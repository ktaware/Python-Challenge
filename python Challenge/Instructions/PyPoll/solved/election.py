import os
import csv

main_csv = os.path.join('..','Resources','election_data.csv') 

with open(main_csv,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    winnerVotes=0
    totalVotes =0
    winnerName = ''
    dict={}
    for row in csvreader:
        totalVotes=totalVotes+1
        candidateName= row[2]
        candidateVotes= row[0]        
        if (candidateName in dict):
            dict[candidateName]+=1
        else:
            dict[candidateName]=1
    print("Election Results")
    print("-------------------------------") 
    print(f"Total Votes: {totalVotes}")
    print("-------------------------------")    
    for candidateName in dict:
       print(f"{candidateName}:  {round(((dict[candidateName]/totalVotes)*100),3)}%  ({dict[candidateName]})")
       
       if (dict[candidateName]> winnerVotes):
            winnerVotes= dict[candidateName]
            winnerName=candidateName
              
    print("-------------------------------")           
    #print("Total Votes:",totalVotes)
    print(f"Winner: {winnerName}")
    print("-------------------------------") 

    

        
