# Use open function to read the content of a file!

# f = open('sample.txt', 'r')
f = open('sample.txt')  #By default the mode is r
data = f.read(5) #read the first 5 characters of the file
print(data)
f.close()