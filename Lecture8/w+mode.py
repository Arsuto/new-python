def example_w_plus_mode():
    with open('example_w+.txt', 'w+') as file:
        file.write("This is the first line.\n")
        file.write("This is the second line.\n")
        file.seek(0)  # Move the cursor to the beginning of the file
        content = file.read()
        print("Content of the file:")
        print(content)

example_w_plus_mode()