#PyBank Analyzes

#import the modules for reading the csv files
import os
import csv
import math


#locate the csv file by defining the path for the file
budget_data = os.path.join("Resources", "budget_data.csv")


#set variables 
total_months = 0
total_net = 0
#average_change = 
#profit_increase = 
#profit_decrease = 

#open csv
with open(budget_data) as csvfile:
        csv_reader = csv.reader(csvfile)

        #remove header from loop 
        csv_header = next(csv_reader)
        
# Find the total months and net total amount 
        for row in csv_reader:
                total_months += 1
                total_net = total_net + int(row[1])
        #print(total_net)
   
#The net total over the entire period

              


            




            





#print results for text file
        print("Financial Analysis")
        print("*********************")
        print(f"Total Months: {total_months}")
        print(f"Total: ${total_net}")
        # print(f"Average Change: {average_change}")
        # print(f"Greatest Increase in Profits: {profit_increase}")
        # print(f"Greatest Decrease in Profits: {profit_decrease}")



