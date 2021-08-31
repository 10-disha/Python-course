#Creating an empty set

b= set()
print(type(b))

#Adding values to an empty set
b.add(4)
b.add(5)
# b.add([3,4,5])
b.add((1,2,3,4,4,4,4))

print(b)

print(len(b)) #prints the length of this set.
b.remove(4) #Removes 5 from set b
print(b)

print(b.pop())
print(b)
