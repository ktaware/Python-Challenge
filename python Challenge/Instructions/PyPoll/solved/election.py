#add our dependencies.
import os
import csv

#Assign a variable to laod a file from a path
main_csv = os.path.join('..','Resources','election_data.csv') 

#Open the election results and read the file
with open(main_csv,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    #Initialize a total vote counter.
    #Winning Candidate and Winning Count Tracker
    winnerVotes=0
    totalVotes =0
    winnerName = ''
    
    #Declare a dictionary
    dict={}
    
    #Print each row in the CSV file.
    for row in csvreader:
        #Add to the total vote count
        totalVotes=totalVotes+1
        #Add a vote to that candidate's count.
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
        #Print the candidate name & percentage of vots.
       print(f"{candidateName}:  {round(((dict[candidateName]/totalVotes)*100),3)}%  ({dict[candidateName]})")
       
       if (dict[candidateName]> winnerVotes):
            winnerVotes= dict[candidateName]
            winnerName=candidateName
              
    print("-------------------------------")           
    #print("Total Votes:",totalVotes)
    print(f"Winner: {winnerName}")
    print("-------------------------------") 

    

        
