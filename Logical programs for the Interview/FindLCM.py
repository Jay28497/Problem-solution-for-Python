# LCM (Least common multiple)

a = int(input("Enter a first number: "))
b = int(input("Enter a second number: "))
if a > b:
    num = a
else:
    num = b

while True:
    if num % a == 0 and num % b == 0:
        print("LCM is: ", num)
        break
    num = num + 1
