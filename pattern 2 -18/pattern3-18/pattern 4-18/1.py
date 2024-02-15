l=int(input("Enter the limit"))
temp=0
for i in range(1,l+1):
    temp=temp+1
    for j in range(l,temp-1,-1):
        print(temp,end=" ")
    print()
temp=l
for i in range(2,l+1):
    temp=temp-1
    for j in range(l,temp-1,-1):
        print(temp,end=" ")
    print()
