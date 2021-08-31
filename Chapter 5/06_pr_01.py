myDict = {
    "pankha" : "fan",
    "dabba" : "box",
    "vastu" : " thing"
}

print("options are", myDict.keys())
a = input("enter hindi word:\n")
#this will throw error if  word is not present 
print("the meaning of your word is: ", myDict[a])

#below line will not throw an error if the key is not present in dictionary 
print("the meaning of your word is: ", myDict.get(a))

