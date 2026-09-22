squares = [x ** 2 for x in range(1,11)]
print(squares)

string = "Hello, World!"
vowels = "aeiouAEIOU"
filtered_string = ''.join([char for char in string if char not in vowels])
print(filtered_string)