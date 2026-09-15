try:
    Value = int(input("Enter a number: "))
    result = 10/Value
except ValueError:
    print("Invalid input! Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("End of program")