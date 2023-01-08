import random

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "AABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "?@#$%\&*/"

use_for_pass = lower_case + upper_case + numbers + symbols
length_pass = 8

password = "".join(random.sample(use_for_pass, length_pass))

print("Your Random Password is : " + password)
