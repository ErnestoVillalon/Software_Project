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

import decimal

# -----------------------------------------------------------------------------
#                                   Sum Function 
# -----------------------------------------------------------------------------

def findSum(str1, str2):


 
	# Create int objects with arbitrary precision
	a = float(str1)
	b = float(str2)
	
	# Add the int objects
	result = a + b

	result = str(result)

	result = three_commas(result, str1, str2)

	# print("result: ", result)
	
	return result

# -----------------------------------------------------------------------------
#                               Difference Function 
# -----------------------------------------------------------------------------

def findDiff(str1, str2):

	# Create int objects with arbitrary precision
	a = float(str1)
	b = float(str2)
	
	# Add the int objects
	result = a - b

	result = str(result)
	
	result = three_commas(result, str1, str2)

	return result
	
# -----------------------------------------------------------------------------
# Funciton to add commas to number stored in string
# Added as part of the requirements update.
# -----------------------------------------------------------------------------

def three_commas(x, str1, str2):

	int1 = float(x)
	decimal_place = compare_decimal(str1, str2)
	out = round(int1, decimal_place)
	# print("round: ", out)
	out = f"{out:,}"
	# print("format: ", out)
	out = str(out)
	return out

# -----------------------------------------------------------------------------
# Funciton to calculate largest decimal place
# -----------------------------------------------------------------------------

def compare_decimal(str1, str2):

	d1 = decimal.Decimal(str1)
	d1 = d1.as_tuple().exponent
	d1 = abs(d1)

	d2 = decimal.Decimal(str2)
	d2 = d2.as_tuple().exponent
	d2 = abs(d2)

	if d1 > d2:
		return d1
	if d2 > d1:
		return d2
	else: 
		return 


