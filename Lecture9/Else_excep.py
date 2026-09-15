try:
    Value = int(input("Enter a number: "))
    result = 10/Value
except ValueError:
    print("Invalid input. Please enter a valid input.")
else:
    print(f"The result of 10 divided by {Value} is {result}")
print("End of program")

def divide (a,b):
    return a/b
a, b = map(int, input().split())
print(divide(a,b))
print("End of program")
