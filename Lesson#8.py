# LESSON # 8 CONTROL MODULES AND FUNCTIONS

# Importing custom modules
import math_operations
import string_operations

# Math functions demo
a = 12
b = 4

print("Addition:", math_operations.add(a, b))
print("Subtraction:", math_operations.subtract(a, b))
print("Multiplication:", math_operations.multiply(a, b))
print("Division:", math_operations.divide(a, b))

# String functions demo
text = "hello world"

print("Capitalized Text:", string_operations.capitalize_text(text))
print("Reversed Text:", string_operations.reverse_text(text))
print("Vowel Count:", string_operations.count_vowels(text))
