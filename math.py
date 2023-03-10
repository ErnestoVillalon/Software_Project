# User Inputs
n1 = int(input("Enter First Number: "))
if n1 > 9999 or n2 > 9999:
    raise Exception("Please input a number less than 10,000!")

n2 = int(input("Enter Second Number: "))
if n1 > 9999 or n2 > 9999:
    raise Exception("Please input a number less than 10,000!")

print("Would you like to add or subtract?")
ch = input("Enter any of these char for specific operation +,- : ")

result = 0
if ch == '+':
    result = n1 + n2
elif ch == '-':
    result = n1 - n2
else:
    print("Input character is not recognized!")

print(n1, ch , n2, ":", result)