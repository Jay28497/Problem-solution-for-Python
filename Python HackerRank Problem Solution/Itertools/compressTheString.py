from itertools import groupby

S = input()
for i, j in groupby(S):
    # print(i)
    # print(list(j))
    # print(len(list(j)))
    print("({}, {})".format(len(list(j)), i), end=" ")
