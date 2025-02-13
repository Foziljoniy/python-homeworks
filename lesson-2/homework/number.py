 #q1
a = float(input("Number : "))
print(round(a, 2))

#q2
a1 = int(input("Number: "))
a2 = int(input("Number: "))
a3 = int(input("Number: "))
print(max(a1, a2, a3))
print(min(a1, a2, a3))

#q3
a4 = float(input("Kilometr"))
print(a4 * 1000, "Meters and ", a4 * 1000000, "santimetr")

#q4
a41 = int(input("Number: "))
a42 = int(input("Number: "))
print(divmod(a41, a42))

#q5
a51 = float(input("Celsiy: "))
faranheit = (a51 *9/5) + 32
print(faranheit)

#q6
a61 = int(input("Number: "))
print(a61%10)

#q7
num7 = int(input("Enter a number: "))
if num7 % 2 == 0:
    print("Even")
else:
    print("Odd")

