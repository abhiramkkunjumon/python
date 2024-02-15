try:
    a=10
    b=0
    c=a/b
    print(c)
except ZeroDivisionError :
    raise ZeroDivisionError ("division by zero")
finally:
    print("hi")
