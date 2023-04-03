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

    Test Case for requirement [SRS-0040]
    1,908,979

## Files

This project will consist of two files:
- math_functions.py
- math_test.py

### math_functions.py

This file will contain three functions findSum, findDiff, and three_commas.

findSum takes two large numbers as string inputs and returns the sum as a string.

findDiff takes two large numbers as string inputs and returns the difference as a string.

three_commas a string input, converts it to an integer, adds commas at every third digit from the end, converts the integer back to a string, and returns it as an output.

### math_test.py

This file contains the test cases for testing the functions in math_functions.py

It hase multiple test cases to verify the funcitonal requirements. To view these requirements, reference document "Software Requirements Specification - Big Number Computation"