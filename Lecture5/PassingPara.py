#def greet(name):
#    print(f"Hello,{name}!")
#greet("Alice")

#def add (a,b):
#    return a+b
#result = add(3,5)
#print(result)

#def greet(name="World"):
#    print(f"Hello,{name}!")
#greet()
#greet("Alice")

#def sum_all(*args):
#    return sum(args)
#print(sum_all(1,2,3,4,5))

#def sum_all(*args):
#    return sum(args)
#print(sum_all(4,5,6,7))

#def find_max(*args):
#    if not args:
#        return None
#    max_Value = args[0]
#    for number in args:
#        if number >max_Value:
#            max_Value = number
#    return max_Value
#result = find_max(3,5,7,2,8)
#print(f"The maximum value is: {result}")

#def print_all(*args):
#    for index, arg in enumerate(args):
#        print(f"Argument {index+1}: {arg}")
#print_all("Python", 3.8, True, [1,2,3], {"key":"value"})

def display_info(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")
display_info(name="Alice", age=30, city="New York")

