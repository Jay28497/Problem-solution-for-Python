a, b = input().split()
arr = input().split()
c = set(input().split())
d = set(input().split())
print(sum((i in c) - (i in d) for i in arr))
