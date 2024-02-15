def factorial(n):
    if n<=1:
        return n
    else:
        return n*factorial(n-1)
s=factorial(5)
print(s)
