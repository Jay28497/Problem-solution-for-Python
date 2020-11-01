def reverse(string):
    string = string[::-1]
    return string


s = input("Enter a string: ")
print(reverse(s))


##################
# Using For Loop #
##################
def reverse(string):
    reverse_string = ""
    for i in string:
        reverse_string = i + reverse_string
    return reverse_string


s = input("Enter a string: ")
print(reverse(s))

####################
# Using While Loop #
####################
s = input("Enter a string: ")
l = len(s) - 1
res = ""
while l >= 0:
    res = res + s[l]
    l = l - 1
print(res)
