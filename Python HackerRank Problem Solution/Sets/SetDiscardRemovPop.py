n = int(input())
s = set(map(int, input().split()))
N = int(input())
for i in range(N):
    c, *args = map(str, input().split())
    getattr(s, c)(*(int(x) for x in args))
print(sum(s))
