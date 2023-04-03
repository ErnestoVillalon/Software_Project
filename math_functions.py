# *****************************************************************************
# CS 5103 Software Project
#
# file: math_functions.py
# author: Ernesto Villalon
#
# Description:
#   
#   This file contains functions to add and subtract very large numbers.
#
# Github: 
#	https://github.com/ErnestoVillalon/Software_Project#software_project
# *****************************************************************************

# -----------------------------------------------------------------------------
#                                   Sum Function 
# -----------------------------------------------------------------------------

def findSum(str1, str2):


 
	# Create int objects with arbitrary precision
	a = int(str1)
	b = int(str2)
	
	# Add the int objects
	result = a + b

	result = str(result)

	result = three_commas(result)
	
	return result

# -----------------------------------------------------------------------------
#                               Difference Function 
# -----------------------------------------------------------------------------

def findDiff(str1, str2):

	# Create int objects with arbitrary precision
	a = int(str1)
	b = int(str2)
	
	# Add the int objects
	result = a - b

	result = str(result)
	
	result = three_commas(result)

	return result
	
# -----------------------------------------------------------------------------
# Funciton to add commas to number stored in string
# Added as part of the requirements update.
# -----------------------------------------------------------------------------

def three_commas(x):

	int1 = int(x)
	out = format (int1, ',d')
	out = str(out)
	return out