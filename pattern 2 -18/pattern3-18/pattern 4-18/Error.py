try:
    a=10
    b=0
    c=a/b
    print(c)
except:
    print("ZeroDivisionError: division by zero")
finally:
    print("Hi")
