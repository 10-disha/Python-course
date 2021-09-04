with open("log.txt") as f:
    content = f.read()

if 'python' in content.upper():
    print("yes python is present")  

else:
    print("no python is not present")      