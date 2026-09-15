try:
    Value = int(input("Enter a number: "))
    result = 10/Value
except Exception as e:
    print(f"An error occurred: {e}")
print("End of program")