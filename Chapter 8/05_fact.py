n = 1
product = 1
for i in range(n):
    product = product * (i+1)
print(product)    


def fact_recur(n):
    if n == 1 or n==0:
        return 1
    return n * fact_recur(n-1)

f = fact_recur(5) 
print(f)   
