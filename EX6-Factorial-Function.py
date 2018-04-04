# Ger O'Mahony

# Exercise 6 Requirements:
# ######################################################################
# Write a Python script containing a function called factorial() that
# takes a single input/argument which is a positive integer and returns
# its factorial. The factorial of a number is that number multiplied by
# all of the positive numbers less than it. For example,the factorial of
# 5 is 5x4x3x2x1 which equals 120. You should, in your script, test the
# function by calling it with the values 5, 7, and 10.
# ######################################################################

def factorial(num_in):

    # check for positive integer first
    if num_in > 0:
        # Calculate the factorial
        num_factorial = 1
        for i in range(1, num_in + 1):
            num_factorial = num_factorial * i

        return num_factorial
    else:
        print('Please enter a positive integer')


print('The factorial of 5 is', factorial(5))
print('The factorial of 7 is', factorial(7))
print('The factorial of 10 is', factorial(10))
print('The factorial of -10 is', factorial(-10))

