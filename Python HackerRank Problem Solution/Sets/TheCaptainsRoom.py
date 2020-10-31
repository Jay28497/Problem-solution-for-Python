a = input()
b = input().split()
s1 = set()
s2 = set()
for i in b:
    if i in s1:
        s2.add(i)
    else:
        s1.add(i)
res = s1.difference(s2)
print(res.pop())
