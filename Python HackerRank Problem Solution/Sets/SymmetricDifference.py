a, b = (int(input()), input().split())
c, d = (int(input()), input().split())
x = set(b)
y = set(d)
p = x.difference(y)
q = y.difference(x)
# print(p)
# print(q)
r = p.union(q)
print("\n".join(sorted(r, key=int)))
