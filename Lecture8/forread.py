with open('example.txt', 'r') as infile:
    lines = infile.readlines()
    for line in lines:
        print(line.strip())