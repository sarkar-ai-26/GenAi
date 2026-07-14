#importing math_utils and its methods
import math_utils
from math_utils import sqaure

#importing string_utils methods
import string_utils

#importing shop_package modules
import shop_package.discount as disc
from shop_package.billing import calculate_total
from shop_package.billing import apply_tax

# Task - 1 Testing modules
print(f"Testing add() module : {math_utils.add(1,5)}")
print(f"Testing subtract() module : {math_utils.subtract(5,2)}")
print(f"Testing square() module : {sqaure(2)}")

#Task - 2 Testing Modules
text = "Testing Modules"
print(f"Testing capitalize_words() module : {string_utils.capitalize_words(text)}")
print(f"Testing reverse_string() module : {string_utils.reverse_string(text)}")
print(f"Testing word_count() module : {string_utils.word_count(text)}")

#Task - 3,4 Testing Modules
print(disc.apply_discount(1000,10))
print(calculate_total([100,200,300]))

