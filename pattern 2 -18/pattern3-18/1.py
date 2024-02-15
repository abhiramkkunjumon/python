l=int(input("Enter the limit"))
temp=l
for i in range(1,l+1):
    temp=temp-1
    for j in range(l,temp,-1):
        print(j,end=" ")
    print()
temp=1
for i in range(l):
    temp=temp+1
    for j in range(l,temp-1,-1):
        print(j,end=" ")
    print()
