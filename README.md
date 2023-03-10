# CS 5103 Software Project

The purpose of this repo is to go through all software engineering practices with a small personal project.

## Topic

The topic of this project is big number computation. It has the following requirement:

"In this project you are performing computation on big numbers (thousands of digits). The initial requirement is to perform addition and subtraction of two numbers."

## Running The Program

To run the test cases, make sure you have Python 3 installed on your system.

In a terminal, navigate to the folder that contains both math_functions.py and math_test.py in the same folder.

Enter the following command

    python3 math_test.py

The terminal should output text similar to this:

    Test Case One: Addition
    198123

    Test Case Two: Subtraction
    991

## Files

This project will consist of two files:
- math_functions.py
- math_test.py

### math_functions.py

This file will contain three functions findSum, findDiff, and isSmaller.

findSum takes two large numbers as string inputs and returns the sum as a string.

findDiff takes two large numbers as string inputs and returns the difference as a string.

isSmaller takes two large numbers as string inputs and returns a boolean value.

### math_test.py

This file contains the test cases for testing the functions in math_functions.py

It hase two test cases. One tests the findSum function and the other tests the findDiff function.