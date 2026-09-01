with open ('employees.txt', 'r') as emp_file:
    for line in emp_file:
        name = line.strip()
        id_num = emp_file.readline().strip()
        dept = emp_file.readline().strip()
        print(f"Name: {name}")
        print(f"ID:   {id_num}")
        print(f"Dept: {dept}")
        print()