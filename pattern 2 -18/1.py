l=int(input("Enter the limit"))
temp=l+1
for i in range(l):
    temp=temp-1
    for j in range(1,temp+1):
        print(j,end=" ")
    print()
for i in range(2,l+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
