#PyBank Analysis

#import the modules
import os
import csv


#locate the csv file by defining the path for the file
budget_data = os.path.join("Resources", "budget_data.csv")
#file = os.path.join("Analysis", "PyBank_Analysis_Results.txt", "w")

#set the variables 
total_months = 0
total_net = 0
avg_change = 0
prev_net = 0
net_chg_list = []
new_mon_total = []
net_increase = ["", 9999999]
net_decrease = ["", 0]
net_average = 0


#open the csv
with open(budget_data) as csvfile:
        csv_reader = csv.reader(csvfile)
        #remove header from loop 
        csv_header = next(csv_reader)

        
# Find the total months and net total amount 
        for row in csv_reader:
                total_months = total_months + 1
                total_net = total_net + int(row[1])
        #print(total_net)
   
# The changes in Profit/Losses and the average of those changes
                #subtract mon1 from mon2 and so forth
                avg_change = int(row[1]) - prev_net
                #print(avg_change)
                prev_net = int(row[1])
                #create a list to hold the new totals from above and then add them
                net_chg_list = net_chg_list + [avg_change]
                #add up all the new totals from month to month
                new_mon_total = new_mon_total + [row[0]]
                #print(new_mon_total)
        
# The greatest increase in revenue and the date/amount
                if avg_change > net_increase[1]:
                        net_increase[1] = avg_change
                        net_increase[0] = row[0]
                #print(avg_change)


# The greatest decrease (lowest increase) in revenue and the date/amount
                if avg_change < net_decrease[1]:
                        net_decrease[1] = avg_change
                        net_decrease[0] = row[0]
        net_average = sum(net_chg_list)/len(net_chg_list)




# Print results
        print('Financial Analysis')
        print('*-*-*-*-*-*-*-*-*-*-*-*-*-*')
        print(f'Total Months: {total_months}')
        print(f'Total: ${total_net}')
        print(f'Average Change: {avg_change}')
        print(f'Greatest Increase in Profits: {net_increase}')
        print(f'Greatest Decrease in Profits: {net_decrease}')


# Export and print results to text file
output = ('Analysis','PyBank_Analysis_Results.txt')
file = open('PyBank_Analysis_Results', 'w')
file.write('Financial Analysis''\n')
file.write('*-*-*-*-*-*-*-*-*-*-*-*-*-*''\n')
file.write(f'Total Months: {total_months}''\n')       
file.write(f'Total: ${total_net}''\n')
file.write(f'Average Change: {avg_change}''\n')
file.write(f'Greatest Increase in Profits: {net_increase}''\n')
file.write(f'Greatest Decrease in Profits: {net_decrease}''\n')

