# Create a program to sum of three number from the user input,
# if user doesn't enter any number', use default as 100, 200, 300

sum1 = int(input("Enter the 1 numbers\n"))
sum2 = int(input("Enter the 2 numbers\n"))
sum3 = int(input("Enter the 3 numbers\n"))

def sum_of_three_numbers(num1=100,num2=200,num3=300):
    return num1+num2+num3

result = sum_of_three_numbers(sum1, sum2, sum3)
print(result)

result2 = sum_of_three_numbers()
print(result2)