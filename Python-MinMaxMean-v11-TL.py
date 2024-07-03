################################ 
# Tom Lutzenberger
# Date: 03/01/2024
# Python-MinMaxMean.py
# Version 1.1
# Description - A simple stats program for crunching the min, max and mean of a variable
# set of numbers provided by the user. Version 1.1 is designed for a singular execution.
# will expand in the future with a looping feature probably until user exits. This version
# added mode and median to the mix.
################################

#standard functions brought in by reference from python libraries
import statistics

# User input to start the program with provided number data
# Program will reject entry if not an integer input and loop for a correct one
def get_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a positive integer greater than zero.")
            else:
                return value
        except ValueError:
            print("Please enter a valid integer.")

# Get input from user on input population count total
num_values = get_input("Enter how many numbers you want to calculate the total of: ")

# Variable declaration
numbers = []

# Loop for number input and output, the loop works while the condition is true until
# the total number of entries criteria provided by the user is met
# Includes input error check
for i in range(1, num_values + 1):
    while True:
        try:
            num = float(input(f"Enter the {i}{'st' if i == 1 else 'th'} number: "))
            numbers.append(num)
            print(num, end=' ')
            break
        except ValueError:
            print("Please enter a valid number.")
print()  

# Output of input data in horizontal format
print("Your numbers provided in horizontal rows that line up and appear as a column:")
print(*numbers, sep=", ")

# Calculating the aggregate input total, max, min, and average
# Note that this version applies statistical fclearunctions already brought in by reference
total = sum(numbers)
max_num = max(numbers)
min_num = min(numbers)
average = statistics.mean(numbers)
mode = statistics.mode(numbers)
median = statistics.median(numbers)

# Printing output to user for calculations
print("\nResults:")
print("Total value for your input:", total)
print("The largest number (max):", max_num)
print("The smallest number (min):", min_num)
print("The average value for input:", average)
print("The mode value for input:", mode)
print("The median value for input:", median)
print("End of program. Thanks for trying it.")

#End program.