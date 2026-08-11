#fruits = ["apple", "banana", "cherry"]
#more_fruits = ["mango", "pineapple"]
#for fruit in more_fruits:
#    fruits.append(fruit)
#print(f"Updated after append : {fruits}")

#berries = ["raspberry","blackberry"]
#berries.insert(1,"strawberry")
#berries.insert(2,"blueberry")
#print(f"Berries after insert : {berries}")

#fruits_with_duplicates = ["apple", "banana", "apple", "cherry", "apple","kiwi"]
#while "apple" in fruits_with_duplicates:
#    fruits_with_duplicates.remove("apple")
#print(f"Fruits after remove : {fruits_with_duplicates}")

#grades = [85, 90, 78, 92, 88]
#third_grade = grades.pop(2)
#grades.append(third_grade)
#print(f"Grades after pop : {grades}")

#animals = ["cat", "dog", "rabbit", "hamster","dog","parrot"]
#first_dog_index = animals.index("dog")
#print(f"The first occurrence of 'dog' is at index: {first_dog_index}")
#second_dog_index = animals.index("dog", first_dog_index + 1)
#print(f"The second occurrence of 'dog' is at index: {second_dog_index}")

#nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#for sublist in nested_list:
#    sublist.clear()
#print(f"Nested list after clear : {nested_list}")  

heroes=['Ironman','Thor','Hulk','Superman','Spiderman']
h2=['Dr.Strange','Cpt. America','Black Panther','Ant Man']

heroes.insert(0,h2[0])
print(heroes.index('Thor'))
heroes.insert(heroes.index('Thor'),h2[1])
print(heroes)
heroes.remove('Superman')
heroes.append('Ant Man')
print(heroes)
heroes.sort()
print(heroes)
heroes.reverse()
print(heroes)
newheroes=heroes
newheroes[0]='Wonder Woman'
print(heroes)
copyheroes=[]+heroes
print(copyheroes)
copyheroes[0]='Hunuman'
print(heroes)
print(copyheroes)