#biggest digit
def big(num):
    temp = num
    big = 0
    while (temp > 0):
        digit = temp % 10
        if big <= digit:
            big = digit
        temp = temp // 10
    return big

num=int(input("Enter the number:"))
biggest=big(num)
print("Biggest number is ",biggest)
