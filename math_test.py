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
#
# Github: 
#	https://github.com/ErnestoVillalon/Software_Project#software_project
# *****************************************************************************
from math_functions import *

if __name__ == "__main__":

    # Test Case One: Addition
    print("Test Case One: Addition")

    str1 = "12345"
    str2 = "1896634"
    print(findSum(str1, str2))
    print(" ")

    # Test Case Two: Subtraction
    print("Test Case Two: Subtraction")

    str1 = "34"
    str2 = "2023"
    print(findDiff(str1, str2))
    print(" ")
