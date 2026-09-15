#try :
#    x = 1/0
#except ZeroDivisionError as e:
#    print(f"Error: {e}")
#print("End of Program")

filename = input('Enter a filename: ')
try:
    infile = open(filename, 'r')
    contents = infile.read()
    print(contents)
    infile.close()
except IOError:
    print('An error occurred trying to read')
    print('The file', filename)

print("End of program")