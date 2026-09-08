setA = {1,2,3,4}
setB = set([8,9,10])

setA.add(5)
setB.update([6,7])
uset = setA | setB
print(uset)
print(len(uset))

setB.update(['ABCD'])
setA.update([6,7,8])
print(setB)

print(setA.intersection(setB))
print(setA ^ setB)