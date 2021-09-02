n=5
def sum(n):
    if n<=1:
        return n
    else:    
        return sum(n-1) + n

f = sum(5) 
print(f)  