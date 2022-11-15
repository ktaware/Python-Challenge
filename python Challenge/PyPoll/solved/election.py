#add our dependencies.
import os
import csv

#Assign a variable to laod a file from a path
main_csv = os.path.join('..','Resources','election_data.csv') 

output_path = os.path.join("..", "analysis", "new.csv")
f = open("C:\Users\xz4w1x\Desktop\Homework\python Challenge\Instructions\PyPoll\analysisel\ection_result.txt", "w")
#Open the election results and read the file
with open(main_csv,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    #Initialize a total vote counter.
    totalVotes =0

    #Winning Candidate and Winning Count Tracker
    winnerName = ''
    winnerVotes=0
    
    #Declare a dictionary
    dict={}

    #Print each row in the CSV file.
    for row in csvreader:
        #Add to the total vote count
        totalVotes=totalVotes+1
         #Print the candidate name from each row.
        candidateName= row[2]
        candidateVotes= row[0]        
        if (candidateName in dict):
            dict[candidateName]+=1
        else:
            dict[candidateName]=1
    print("Election Results\n")
    print("-------------------------------\n") 
    print(f"Total Votes: {totalVotes}")
    print("-------------------------------\n")    
    for candidateName in dict:
       print(f"{candidateName}:  {round(((dict[candidateName]/totalVotes)*100),3)}%  ({dict[candidateName]})")
       
       if (dict[candidateName]> winnerVotes):
            winnerVotes= dict[candidateName]
            winnerName=candidateName
              
    print("-------------------------------\n")           
    #print("Total Votes:",totalVotes)
    print(f"Winner: {winnerName}")
    print("-------------------------------\n") 

    f.write("Election Results\n")
    f.write("-------------------------------\n") 
    f.write(f"Total Votes: {totalVotes}\n")
    f.write("-------------------------------\n")    
    for candidateName in dict:
       f.write(f"{candidateName}:  {round(((dict[candidateName]/totalVotes)*100),3)}%  ({dict[candidateName]})\n")
       
       if (dict[candidateName]> winnerVotes):
            winnerVotes= dict[candidateName]
            winnerName=candidateName
              
    f.write("-------------------------------\n")           
    #print("Total Votes:",totalVotes)
    f.write(f"Winner: {winnerName}\n")
    f.write("-------------------------------\n") 

    

        