#######################################################
#  PROGRAM: P5
#
#  PURPOSE: Euler Project Problem 5 - Smallest multiple
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
divisor = [False] * 10

while True:

    num += 2520
    divisor = [False for item in divisor]

    for i in range(11, 21):
        if num % i == 0:
            divisor[i-11] = True
        else:
            break

    if all(divisor):
        break

print('Smallest positive number is: ' + str(num))

