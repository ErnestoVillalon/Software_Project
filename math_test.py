# *****************************************************************************
# CS 5103 Software Project
#
# file: math_test.py
# author: Ernesto Villalon
#
# Description:
#   
#   This contains test cases to test the functionality of the funcitons in
#   math_functions.py
#   
#   These functions include
#       - The addidtion of large numbers
#       - The subtraction of large numbers
# *****************************************************************************
from math_functions import *

if __name__ == "__main__":

    # Test Case One: Addition
    print("Test Case One: Addition")

    str1 = "12"
    str2 = "198111"
    print(findSum(str1, str2))
    print(" ")

    # Test Case Two: Subtraction
    print("Test Case Two: Subtraction")

    str1 = "88"
    str2 = "1079"
    print(findDiff(str1, str2))
    print(" ")
