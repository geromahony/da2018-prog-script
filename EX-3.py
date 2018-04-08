# Ger O'Mahony
# Collatz Conjecture

# Exercise 3 Requirements:
# ############################################################
# Complete the exercise discussed in the Collatz conjecture 
# video by writing a single Python script that starts with 
# an integer and repeatedly applies the Collatz function 
# (divide by 2 if even, multiply by three and 1 if odd) 
# using a while loop and if statement. At each iteration, 
# the current value of the integer should be printed to the 
# screen. You can specify in your code the starting value 
# of 17. If you wish to enhance your program, have the program 
# ask the user for the integer instead of specifying a value 
# at the start of your code. 
# ############################################################

import sys
import time

# Ask user for integer input
# Use try catch for input errors
try:
    num = int(input('Enter starting integer: '))

except Exception:
    print('Only integers are accepted. Exiting program')
    time.sleep(2)
    sys.exit(0)

# No negative numbers allowed
if num < 0:
    print('Number needs to be a positive integer')

# Keep looping while the number is greater than
# 1 using a while loop
while num > 1:

    # Display the number
    print(int(num))

    # If the number is even 
    # the modulo will be zero
    # then divide by 2
    if num % 2 == 0:
        num = num / 2
    # Otherwise the number is not even
    # so multiply by 3 and add 1
    else:
        num = num * 3 + 1

# Display the last number outside the while loop
print(int(num))


