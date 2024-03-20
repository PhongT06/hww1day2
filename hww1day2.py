
number = int(input("Enter a number: "))
if number > 0:
    print("This number is positive!")
elif number == 0:
    print("This number is zero")
else:
    print("This number is negative")

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
num3 = input("Enter the third number: ")

if num1 == num2 == num3:
    print("All numbers are equal")
elif num1 == num2 or num1 == num3 or num2 == num3:
    print("Two numbers are equal.")
largest_number = max(num1, num2, num3)
print("The largest number is:", largest_number)
smallest_number = min(num1, num2, num3)
print("The smallest number is:", smallest_number)

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, " is a leap year.")
else:
    print(year,  "is not a leap year.")

