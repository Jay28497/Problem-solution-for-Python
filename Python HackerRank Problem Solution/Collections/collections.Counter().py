# >>> from collections import Counter
# >>>
# >>> myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
# >>> print Counter(myList)
# Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})
# >>>
# >>> print Counter(myList).items()
# [(1, 3), (2, 4), (3, 4), (4, 2), (5, 1)]
# >>>
# >>> print Counter(myList).keys()
# [1, 2, 3, 4, 5]
# >>>
# >>> print Counter(myList).values()
# [3, 4, 4, 2, 1]


from collections import Counter

n = int(input())
s = Counter(map(int, input().split()))
c = int(input())
total = []

for i in range(c):
    a, b = map(int, input().split())
    if s[a] > 0:
        total.append(b)
        s.subtract(Counter([a]))
    else:
        pass
print(sum(total))
