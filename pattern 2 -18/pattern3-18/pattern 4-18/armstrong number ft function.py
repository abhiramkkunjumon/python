def arm(num,length):
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum = sum + (digit ** length)
        temp = temp // 10
    if num == sum:
        print("armstrong")
    else:
        print("not armstrong")

num=input("Enter the number: ")
length=len(num)
num=int(num)
arm(num,length)
