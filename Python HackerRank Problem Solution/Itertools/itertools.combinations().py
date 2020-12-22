# >>> from itertools import combinations
# >>>
# >>> print list(combinations('12345',2))
# [('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '4'),
#  ('3', '5'), ('4', '5')]
# >>>
# >>> A = [1,1,3,3,3]
# >>> print list(combinations(A,4))
# [(1, 1, 3, 3), (1, 1, 3, 3), (1, 1, 3, 3), (1, 3, 3, 3), (1, 3, 3, 3)]

from itertools import combinations

S, k = input().split(" ")

for i in range(1, int(k) + 1):
    for j in combinations(sorted(S), i):
        print(''.join(j))
