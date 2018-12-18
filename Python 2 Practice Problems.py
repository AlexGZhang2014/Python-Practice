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

4. Define a function factorial that takes an integer x as input. Calculate and return the factorial of that number.

def factorial(x):
  total = 1
  while x > 1:
    total *= x
    x -= 1
  return total

5. Define a function called is_prime that takes a number x as input. For each number n from 2 to x - 1, test if x is evenly divisible by n.
If it is, return False. If none of them are, then return True.

def is_prime(x):
  if x < 2:
    return False
  else:
    for n in range(2, x-1):
      if x % n == 0:
        return False
    return True

print is_prime(13)
print is_prime(10)

6. Define a function called reverse that takes a string textand returns that string in reverse. For example: reverse("abcd") should return "dcba".
You may not use reversed or [::-1] to help you with this. You may get a string containing special characters (for example, !, @, or #).
                                                                                                              
def reverse(text):
  reversed_string = ""
  for char in text:
    reversed_string = char + reversed_string
  return reversed_string                                                                                                              

7. Define a function called anti_vowel that takes one string, text, as input and returns the text with all of the vowels removed.
For example: anti_vowel("Hey You!") should return "Hy Y!". Don't count Y as a vowel. Make sure to remove lowercase and uppercase vowels.
                                                                                                              
def anti_vowel(text):
  result = ""
  vowels = "aeiouAEIOU"
  for letter in text:
    if letter not in vowels:
      result += letter
  return result

print(anti_vowel("Hey You!"))
print(anti_vowel("Hey look, words!"))
