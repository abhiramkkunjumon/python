n=int(input("Enter the number"))
lrg=0
   while n!=0:
    d=n%10
   if lrg<d:
        lrg=d
   n//10
    print(lrg)
