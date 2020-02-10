# Purpose -
# Write a program that uses nested loops to collect data
# and calculate the average rainfall over a period of years.
# The program should first ask for the number of years.
# The outer loop will iterate once for each year.
# The inner loop will iterate twelve times, once for each month.
# Each iteration of the inner loop will ask the user for the inches of rainfall
# for that month.
# After all the iterations, the program should display the number of months,
# the total inches of rainfall,
# and the average rainfall per month for the entire period.
#
# Specifications
# Assume the user will enter valid data (Integer/Float).
# The outer loop will iterate once for each year and
# the inner loop will iterate twelve times once for each month.
# Assume the user will enter 1 or more number of years for number of years.
# Assume the user will enter positive number
# ( 0.00 or more) for rainfall in inches for each month.
# The program should round the rainfall average to a maximum of two decimal
# places.

_years = input(print("Please enter the number of years : "))
_number_months = _years*12
print(_number_months)
