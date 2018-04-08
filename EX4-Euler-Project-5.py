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

# Note for Ian:
# I have previous programming experience in Fortran (it still exists!)
# I have programmed the first 20 or so Euler project problems
# in Fortran for my own practice previously. When writing this in
# Python, I used my Fortran code as reference ( I will post it below
# for reference)
# I also developed the code locally and pushed the final code to the GitHub
# repo so you can't really see the progression in my work. I didn't realise
# I had to push incrementally to illustrate this at the time and as I had
# already committed my code and made the optimisations to speed things up.
# Specifically, the incrementing by 2520 as suggested by David Zaslavsky
# as posted in the Stackoverflow answer referenced below.
# The optimised Python code runs way faster than my initial attempt in Fortran.

num = 0
# Initialise logical list of 10 elements
divisor = [False] * 10

while True:

    # Start at 2520 as that's divisible by
    # 1 - 10 and increment by this as
    # result must be a multiple [1]
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

# References
# [1] https://stackoverflow.com/questions/8024911/project-euler-5-in-python-how-can-i-optimize-my-solution/8025847#8025847


# Fortran Code:

#    program P5
#
#    implicit none
#
#    ! Variables
#    logical, dimension(20) :: divisors
#    integer :: i, num
#    num = 1
#    do
#      divisors = .false.
#      do i = 1, 20
#        if( mod(num, i) == 0 ) divisors(i) = .true.
#      end do
#      if( all(divisors) )exit
#      num = num + 1
#    end do
#    print '("Number:", i10)', num
#
#    end program P5

