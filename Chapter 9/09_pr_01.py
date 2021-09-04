f = open('poem.txt')
t = f.read()
if 'twinkle' in t:
    print("twinkle is present")
else:
    print("not present")
f.close()        