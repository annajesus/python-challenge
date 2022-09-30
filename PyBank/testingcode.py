#PyBank Analyzes

#import the modules for reading the csv files
import os
import csv
#import math


#locate the csv file by defining the path for the file
budget_data = os.path.join("Resources", "budget_data.csv")


#set variables 
total_months = 0
total_net = []
# total_profits = []
# total_revenue = []
#average_change = 
#profit_increase = 
#profit_decrease = 

#open csv
with open(budget_data) as csvfile:
        csv_reader = csv.reader(csvfile)

        #remove header from loop 
        csv_header = next(csv_reader)

# The total number of months included in the dataset         
        for row in csv_reader:
            total_months += 1
        print(total_months)

# The net total amount of "Profit/Losses" over the entire period
        for row in csv_reader:
                if total_net == 1:
                        total_net += int(row[1])
                print(total_net)


#The changes in Profit/Losses and the average of those changes over the entire period 











#set variable        
#totalprofit = 0   
#date = []
#profits = []   
        
        #loop thru each row and total the profit/losses
        #total_net = total_net + int(row["Profit/Losses"])
# for row in csv_header:
#     total_net = total_net + int(row[1])
#           date.append(row[0])
#            profit = int(row[1])
#         profits.append(profit)
