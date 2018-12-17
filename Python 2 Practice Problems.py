1. Define a function is_even that will take a number x as input.
If x is even, then return True. Otherwise, return False.

def is_even(x):
  if x % 2 == 0:
    return True
  else:
    return False

2. Define a function is_int that takes a number x as an input.
Have it return True if the number is an integer (as defined above) and False otherwise.

For example:

is_int(7.0)   # True    
is_int(7.5)   # False    
is_int(-1)    # True

def is_int(x):
  if int(x) == x:
    return True
  else:
    return False

3. Write a function called digit_sum that takes a positive integer n as input and returns the sum of all that number's digits.
For example: digit_sum(1234) should return 10 which is 1 + 2 + 3 + 4.
(Assume that the number you are given will always be positive.)

def digit_sum(n):
  total = 0
  str_num = str(n)
  for num in str_num:
    total += int(num)
  return total
