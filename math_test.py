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

    print(" ")
    print("Requirements [SRS-0010]-[SRS-0030] are verified through each of the proceeding test cases.")
    print(" ")

    #[SRS-0040] If two positive numbers are provided as input for addition, the program shall return a positive number as an output.
    print("Test Case for requirement [SRS-0040]")

    str1 = "12345"
    str2 = "1896634"
    print(findSum(str1, str2))
    print(" ")

    #[SRS-0050] If two negative numbers are provided as input for addition, the program shall return a negative number as an output.
    print("Test Case for requirement [SRS-0050]")

    str1 = "-12345"
    str2 = "-1896634"
    print(findSum(str1, str2))
    print(" ")

    #[SRS-0060] If two numbers of opposite polarity are provided as input for addition, and the negative numbers is lesser than the positive number, the program shall return a positive number as an output.
    print("Test Case for requirement [SRS-0060]")

    str1 = "-12345"
    str2 = "1896634"
    print(findSum(str1, str2))
    print(" ")

    #[SRS-0070] If two numbers of opposite polarity are provided as input for addition, and the negative numbers is greater than the positive number, the program shall return a negative number as an output.
    print("Test Case for requirement [SRS-0070]")

    str1 = "12345"
    str2 = "-1896634"
    print(findSum(str1, str2))
    print(" ")

    #[SRS-0080] If two positive numbers are provided as input for subtraction, and the second number is lesser than the first, the program shall return a positive number as an output.
    print("Test Case for requirement [SRS-0080]")

    str1 = "342987947"
    str2 = "2023"
    print(findDiff(str1, str2))
    print(" ")

    #[SRS-0090] If two positive numbers are provided as input for subtraction, and the second number is greater than the first, the program shall return a negative number as an output.
    print("Test Case for requirement [SRS-0090]")

    str1 = "2023"
    str2 = "342987947"
    print(findDiff(str1, str2))
    print(" ")

    #[SRS-0100] If two numbers of opposite polarity are provided as input for subtraction, and the second number is a negative number, the program shall return a positive number as an output.
    print("Test Case for requirement [SRS-0100]")

    str1 = "2023"
    str2 = "-342987947"
    print(findDiff(str1, str2))
    print(" ")

    #[SRS-0110] If two numbers of opposite polarity are provided as input for subtraction, and the first number is a negative number, the program shall return a negative number as an output.
    print("Test Case for requirement [SRS-0110]")

    str1 = "-2023"
    str2 = "342987947"
    print(findDiff(str1, str2))
    print(" ")

    #[SRS-0140] When performing arithmetic functions on the two input numbers, the output shall have the same number of decimal places as the input number with the larger decimal place.
    print("Test Case for requirement [SRS-0140] (Addition)")

    str1 = "23.00000008"
    str2 = "562.56708"
    print(findSum(str1, str2))
    print(" ")

   #[SRS-0140] When performing arithmetic functions on the two input numbers, the output shall have the same number of decimal places as the input number with the larger decimal place.
    print("Test Case for requirement [SRS-0140] (Subtraction)")

    str1 = "23.007"
    str2 = "562.55555"
    print(findDiff(str1, str2))
    print(" ")
