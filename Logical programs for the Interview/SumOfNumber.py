num = int(input("Enter a number: "))
if num < 0:
    print("Enter a positive number")
else:
    sum = 0
    while num > 0:
        sum += num
        num -= 1
    print("The sum is", sum)


###########################################################
def findSum(n):
    return n * (n + 1) / 2


n = int(input("Enter a number: "))
print(findSum(n))


###########################################################
def sum(n):
    total = 0
    for i in range(1, n + 1):
        total += i


n = int(input("Enter a number: "))
print(sum(n))
