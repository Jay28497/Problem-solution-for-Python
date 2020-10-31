a = int(input())

for i in range(a):
    b = int(input())
    x = set(input().split())
    c = int(input())
    y = set(input().split())
    print(x.issubset(y))
