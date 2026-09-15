try:
    value = int(input("Enter a number: "))
    result = 10 / value
except ValueError:
    print("Invalid input. Please enter valid integers.")
except ZeroDivisionError:
    print("Division by zero is not allowed. please enter a non-zero integer.")
else:
    print(f"The result of 10 divided by {value} is {result}")
finally:
    print("Execution of the try-except block is complete. Program continues.")

print("End of program.")