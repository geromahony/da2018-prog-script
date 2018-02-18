# Ger O'Mahony
# Collatz Conjecture
import sys

try:
    num = int(input('Enter starting integer: '))
except ValueError:
    print('Only integers are accepted. Exiting program')
    sys.exit(0)

if num < 0:
    print('Number needs to be a positive integer')

while num > 1:

    print(int(num))

    if num % 2 == 0:
        num = num / 2
    else:
        num = num * 3 + 1

print(int(num))


