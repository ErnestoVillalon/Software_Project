# *****************************************************************************
# CS 5103 Software Project
#
# file: math_functions.py
# author: Ernesto Villalon
#
# Description:
#   
#   This file contains functions to add and subtract very large numbers.
# *****************************************************************************

# -----------------------------------------------------------------------------
#                                   Sum Function 
# -----------------------------------------------------------------------------

def findSum(str1, str2):

	# Before proceeding further, make sure length
	# of str2 is larger.
	if len(str1)> len(str2):
		temp = str1
		str1 = str2
		str2 = temp

	# Take an empty string for storing result
	str3 = ""

	# Calculate length of both string
	n1 = len(str1)
	n2 = len(str2)
	diff = n2 - n1

	# Initially take carry zero
	carry = 0

	# Traverse from end of both strings
	for i in range(n1-1,-1,-1):
	
		# Do school mathematics, compute sum of
		# current digits and carry
	
		sum = ((ord(str1[i])-ord('0')) +
				int((ord(str2[i+diff])-ord('0'))) + carry)
	
		str3 = str3+str(sum%10 )
		
		
		carry = sum//10

	# Add remaining digits of str2[]
	for i in range(n2-n1-1,-1,-1):
	
		sum = ((ord(str2[i])-ord('0'))+carry)
		str3 = str3+str(sum%10 )
		carry = sum//10

	# Add remaining carry
	if (carry):
		str3+str(carry+'0')

	# reverse resultant string
	str3 = str3[::-1]

	return str3

# -----------------------------------------------------------------------------
#                               Differenct Function 
# -----------------------------------------------------------------------------

def findDiff(str1, str2):
	
	# Before proceeding further,
	# make sure str1 is not smaller
	if (isSmaller(str1, str2)):
		str1, str2 = str2, str1

	# Take an empty string for
	# storing result
	Str = ""
	
	# Calculate lengths of both string
	n1 = len(str1)
	n2 = len(str2)
	diff = n1 - n2
	
	# Initially take carry zero
	carry = 0
	
	# Traverse from end of both strings
	for i in range(n2 - 1, -1, -1):
		
		# Do school mathematics, compute
		# difference of current digits
		# and carry
		sub = ((ord(str1[i + diff]) - ord('0')) -
			(ord(str2[i]) - ord('0')) - carry)

		if (sub < 0):
			sub += 10
			carry = 1
		else:
			carry = 0

		Str += chr(sub + ord('0'))
	
	# Subtract remaining digits of str1[]
	for i in range(n1 - n2 - 1, -1, -1):
		if (str1[i] == '0' and carry):
			Str += '9'
			continue
			
		sub = (ord(str1[i]) - ord('0')) - carry
		
		# Remove preceding 0's
		if (i > 0 or sub > 0):
			Str += chr(sub + ord('0'))
			
		carry = 0

	# Reverse resultant string
	Str = Str[::-1]
	
	return Str

# -----------------------------------------------------------------------------
#                   Function to decide which string is smaller 
# -----------------------------------------------------------------------------

def isSmaller(str1, str2):
	
	# Calculate lengths of both string
	n1 = len(str1)
	n2 = len(str2)

	if (n1 < n2):
		return True
	if (n2 < n1):
		return False

	for i in range(n1):
		if (str1[i] < str2[i]):
			return True
		elif (str1[i] > str2[i]):
			return False
			
	return False