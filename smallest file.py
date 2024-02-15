n=int(input("Enter the number"))
sml=0
while n!=0:
    d=n%10
    if sml<d:
        sml=d
    n//=10
    print(sml)
