def format_strings(*args):
    text = "".join(args)
    text = text.replace(" ", "-")
    return text.upper()

result = format_strings("Hello", "world", "this", "is", "a", "test")
print(result)  # Output: "HELLOWORLDTHISISATEST"
result = format_strings("Python", "is", "fun")
print(result)  # Output: "PYTHONISFUN"
result = format_strings("Hello world")
print(result)  # Output: "HELLO-WORLD"
