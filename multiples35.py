'''If we list all the natural numbers below that are multiples of 3 or 5, we get 3,6, 5, 9.
The sum of these multiples is 23
.

Find the sum of all the multiples of 3 or 5 below 1000
'''

numbers = [number for number in range(1000) if (number %3 ==0 or number %5 == 0)]

total = sum(numbers)
print(total)