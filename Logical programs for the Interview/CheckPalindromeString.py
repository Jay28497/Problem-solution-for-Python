x = input("Enter the string: ")

w = ""
for i in x:
    w = i + w

if x == w:
    print("String is a palindrome")
else:
    print("String is not palindrome")
