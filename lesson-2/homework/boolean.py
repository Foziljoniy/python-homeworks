#q1
name = input("Name")
password = input("Pasword")
if name and password:
    print("accept")

#q2
q21 = int(input("Number: "))
q22 = int(input("Number: "))
if q21 == q22:
    print("equal")

#q3
q31 = int(input("Number: "))
if q31>0 and (q31%2==0):
    print("Positive and Even")
else:
    print("not positive and not even")

#q4
q41 = int(input("1: "))
q42 = int(input("2: "))
q43 = int(input("3: "))
if q41 != q42 and q42 != q43 and q41 != q43:
    print("different")
else:
    print("not different")

#q5
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
    if len(str1) == len(str2):
        return "Strings have the same length."
    else:
        return "Strings have different lengths."

#q6
num61 = int(input("Enter a number: "))
    if number61 % 3 == 0 and number61 % 5 == 0:
        return "The number is divisible by both 3 and 5."
    else:
        return "The number is not divisible by both 3 and 5."c%5 == 0 and c%3 ==0

#q7
def check_divisibility(number):
    if number % 3 == 0 and number % 5 == 0:
        return "The number is divisible by both 3 and 5."
    else:
        return "The number is not divisible by both 3 and 5."

def check_sum_greater_than_50_8(num1, num2):
    return "Sum is greater than 50.8." if (num1 + num2) > 50.8 else "Sum is not greater than 50.8."

def check_between_10_and_20(number):
    return "The number is between 10 and 20." if 10 <= number <= 20 else "The number is not between 10 and 20."

# Taking input from the user
num = int(input("Enter a number: "))
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Checking conditions and displaying results
print(check_divisibility(num))
print(check_sum_greater_than_50_8(num1, num2))
print(check_between_10_and_20(num))
