#Find max between 3 numbers

#logic building
#user inputs _ num1, num2, num3 - int
#o\p - int or string with max num

#logic if else - condition
#syntax
#if condition 1:
#   print("do 1")
#elif condition 2:
#   print("do 2")
#elif condition3:
#   print("do 3")
# print("do for else")

num1 = int(input("Enter the number1\n"))
num2 = int(input("Enter the number2\n"))
num3 = int(input("Enter the number3\n"))

if num1 > num2 and num1 > num3:
    print("MAx is ",num1)
elif num2 > num1 and num2 > num3:
    print("Max is ",num2)
else:
    print("Max is ",num3)

