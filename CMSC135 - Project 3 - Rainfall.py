# CMSC135 Project 3 
# Purpose -
# Write a program that uses nested loops to collect data
# and calculate the average rainfall over a period of years.

# Declare variables
# The rainfall_Total variable is for the total amount rainfall
rainfall_Total = float(0.00)
# The rainfall_Monthly variable collects the input for each month
rainfall_Monthly = float(0.00)
# The rainfall_Average variable calculates the average accross all of the years
rainfall_Average = float(0.00)
# The years variable defines how many times the outer loop, loops
years = int(0)
# The months_Total variable is the counter to track the total number of months
months_Total = int(0) #accuminlator, counter to track months


# This is where the user informs how many years to collect the information
years = int(input("How many years will we be collecting data for? "))

# This is the outer loop that runs once per year, as defined by years variable
for year in range(years):
   # Display which year data is being collected for
    print ("Collecting the data for year ", year + 1)
   # This is the inner loop that runs twelve times, once for each month in a year
    for month in range(12):
      # This is where the user enters the monthly rainfall for each month
        rainfall_Monthly = float(input("Please enter the rainfall for this month : "))
      # This is the months counter that accuminlates the total of been recorded
        months_Total += 1
      # Adding the the monthly rainfall to the running total
        rainfall_Total += rainfall_Monthly

# Calculating the average monthly rainfall from accross the year(s)
rainfall_Average = rainfall_Total / months_Total

# Display the total number of months data has been collected for
print("Data was collected for", years, "years or" ,months_Total, "months.")

# Display the total amount of rainfall with the variable rainfall_Total
print("The total amount of rainfall was", format(rainfall_Total, ".2f"), "inches.")

# Display the average monthly rainfall from accross the year(s)
print("The average monthly rainfall was",format(rainfall_Average, ".2f"),"inches.")
