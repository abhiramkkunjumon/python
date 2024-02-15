def odd_even(n):
    if not isinstance(n,int):
     pass
     # raise ValueError("input must be an integer")
    if n%2==0:
      print("Even")
    else:
        print("Odd")
try:
    n=int(input("Eneter the name"))
    odd_even(n)
except ValueError as v:
    raise ValueError (v)
