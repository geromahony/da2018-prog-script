#######################################################
#
#  Euler Project Problem 5 - Smallest multiple
#
#  PROBLEM STATEMENT:
#
#  2520 is the smallest number that can be divided by
#  each of the numbers from 1 to 10 without any remainder.
#
#  What is the smallest positive number that is evenly
#  divisible by all of the numbers from 1 to 20?
#
#######################################################

num = 0
# Initialise logical list of 10 elements
divisor = [False] * 10

while True:

    # Start at 2520 as that's divisible by
    # 1 - 10 and increment by this as
    # result must be a multiple
    num += 2520

    # Reset logical list every iteration
    divisor = [False for item in divisor]

    # Loop over range 11 - 20
    for i in range(11, 21):
        # Modulo = 0 if divisible
        if num % i == 0:
            divisor[i-11] = True
        else:
            break
    # Check if list of divisors is all true
    if all(divisor):
        break

print('Smallest positive number is: ' + str(num))

