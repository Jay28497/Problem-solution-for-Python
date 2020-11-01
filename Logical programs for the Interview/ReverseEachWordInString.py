def reverseWord(s):
    return ' '.join(word[::-1] for word in s.split(" "))


s = "I love India"
print(reverseWord(s))


###########################################################
s = "I am Python Developer"
print(' '.join(x[::-1] for x in s.split(" ")))
