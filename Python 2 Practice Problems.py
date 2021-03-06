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

8. Define a function scrabble_score that takes a string word as input and returns the equivalent scrabble score for that word.

Assume your input is only one word containing no spaces or punctuation.
As mentioned, no need to worry about score multipliers!
Your function should work even if the letters you get are uppercase, lowercase, or a mix.
Assume that you're only given non-empty strings.
                                                                                                              
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}

def scrabble_score(word):
  total = 0
  lower_word = word.lower()
  for letter in lower_word:
    total += score[letter]
  return total                                                                                                           

9. Write a function called censor that takes two strings, text and word, as input.
It should return the text with the word you chose replaced with asterisks.

For example: censor("this hack is wack hack", "hack") should return: "this **** is wack ****"
                                                                                                              
Assume your input strings won't contain punctuation or upper case letters.
The number of asterisks you put should correspond to the number of letters in the censored word.
                                                                                                              
def censor(text, word):
  asterisks = "*" * len(word)
  text_array = text.split(" ")
  for index, item in enumerate(text_array):
    if item == word:
      text_array.remove(item)
      text_array.insert(index, asterisks)
  return " ".join(text_array)

print(censor("this hack is wack hack", "hack"))

10. Define a function called count that has two arguments called sequence and item.
Return the number of times the item occurs in the list.
For example: count([1, 2, 1, 1], 1) should return 3 (because 1 appears 3 times in the list).
                                                                                                              
def count(sequence, item):
  count = 0
  for thing in sequence:
    if thing == item:
      count += 1
  return count

11. Define a function called purify that takes in a list of numbers, removes all odd numbers in the list, and returns the result.
For example, purify([1,2,3]) should return [2].
Do not directly modify the list you are given as input; instead, return a new list with only the even numbers.
                                                                                                              
def purify(numbers):
  final = []
  for num in numbers:
    if num % 2 == 0:
      final.append(num)
  return final
                                                                                                              
12. Define a function called product that takes a list of integers as input and returns the product of all of the elements in the list.
For example: product([4, 5, 5]) should return 100 (because 4 * 5 * 5 is 100).

def product(numbers):
  product = 1
  for num in numbers:
    product *= num
  return product

13. Write a function remove_duplicates that takes in a list and removes elements of the list that are the same.
For example: remove_duplicates([1, 1, 2, 2]) should return [1, 2].

def remove_duplicates(elements):
  result = []
  for elem in elements:
    if elem not in result:
      result.append(elem)
  return result                                                                                                              

14. Write a function called median that takes a list as an input and returns the median value of the list. For example: median([1, 1, 2]) should return 1.
The list can be of any size and the numbers are not guaranteed to be in any particular order. Make sure to sort it!
If the list contains an even number of elements, your function should return the average of the middle two.
                                                                                                              
def median(numbers):
  sort_nums = sorted(numbers)
  if len(sort_nums) < 2:
    return sort_nums[0]
  elif len(sort_nums) % 2 == 0:
    return (sort_nums[len(sort_nums)/2] + sort_nums[len(sort_nums)/2-1])/2.0
  else:
    return sort_nums[len(sort_nums)/2] 
