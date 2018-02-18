# A program that displays Fibonacci numbers using people's names.

# Exercise 1 - Discussion Board Post:
#####################################
# Re: Fibonacci exercise responses
# by GERARD O MAHONY - Monday, 22 January 2018, 10:08 PM
# My name is Gerard, so the first and last letter of my name (G + D = 7 + 4) give the number 11.
# The 11th Fibonacci number is 89.

# Exercise 2 - Discussion Board Post:
#####################################
# Re: Week 2 task
# by GERARD O MAHONY - Monday, 29 January 2018, 7:53 PM
# My surname is OMahony
# The first letter O is number 79
# The last letter y is number 121
# Fibonacci number 200 is 280571172992510140037611932413038677189525

# ord() is a built in Python function. The method takes a character input and returns an integer number
# which is a numerical representation of the character in the American Standard Code for 
# Information Interchange [ASCII] character set. 
# This is how computers understand characters - as a numerical representation [in binary]. 


def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i

name = "OMahony"
first = name[0]
last = name[-1]
firstno = ord(first)
lastno = ord(last)
x = firstno + lastno

ans = fib(x)
print("My surname is", name)
print("The first letter", first, "is number", firstno)
print("The last letter", last, "is number", lastno)
print("Fibonacci number", x, "is", ans)

