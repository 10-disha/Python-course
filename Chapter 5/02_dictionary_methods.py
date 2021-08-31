myDict = {
    "Fast": "In a Quick Manner",
    "Harry": "A coder",
    "marks" : [1,3,4],
    "anotherdict" : {'harry':'Player'},
    1:2
}

#Dictionary methods
print(list(myDict.keys())) #print the keys of the dictionary
print(list(myDict.values())) #print the values of the dictionary
print(list(myDict.items())) #print the key, value of the dictionary
print(myDict)

updateDict = {
    "lovish" : "friend",
    "Harry" : " A Dancer"
}
myDict.update(updateDict) #update dictionary by adding key - value pairs from updateDict
print(myDict)
print(myDict.get("Harry"))

 #get will not throw error if key is not present it will simple show none.
 
