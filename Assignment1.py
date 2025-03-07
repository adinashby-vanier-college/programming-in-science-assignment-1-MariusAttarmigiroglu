# Function 1: Using Python built-in functions
# This function should take three numbers as input and return their max.
def built_in_functions_max(num1, num2, num3):
    numbers = (num1, num2, num3)
    max_value = max(numbers)
    return max_value
 
# Function 2: Using Python built-in functions
# This function should take three numbers as input and return their min.
def built_in_functions_min(num1, num2, num3):
    numbers = (num1, num2, num3)
    min_value = min(numbers)
    return min_value

# Function 3: Conditional Statements – The If Statement
# This function should check if a number is positive, negative, or zero and return the corresponding message.
def check_number(number):
  a = 0 
  if number > a: 
    return "Positive"
  if number < a: 
    return "Negative"
  if number == a:
    return "Zero"

# Function 4: For Loop – Making a Star Shape
# This function should return a string representing a star shape.
def star_shape(rows):
    result = ""
    for i in range(1, rows +1):
        result += "*" * i + "\n"
    return result.strip("\n")

# Function 5: While Loop – Counting Multiples of 3
# This function should return a list of numbers from 1 to limit, replacing multiples of 3 with "Multiple of 3".
def count_multiples_of_3(limit):
    result = ""
    for number in range(1, limit + 1):
        if number % 3 == 0:
            result += "Multiple of 3\n"
        else:
            result += str(number)+ "\n"
    return result.strip()

# Function 6: Sum of Even Numbers in a Range
# This function should calculate and return the sum of even numbers within a given range.
def sum_of_even_numbers(start, end):
    numbers = []
    for i in range(start, end + 1):
        if i % 2 == 0:
            numbers.append(i)
        result = sum(numbers)
    return result
