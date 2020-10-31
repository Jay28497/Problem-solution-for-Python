a = set(map(int, input().split()))
n = int(input())
f = 0
for i in range(n):
    b = set(map(int, input().split()))
    if len(b.difference(a)) != 0:
        f = 1
    else:
        if len(b) == len(a):
            f = 1
if f == 0:
    print("True")
else:
    print("False")
