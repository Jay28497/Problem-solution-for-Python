from collections import Counter, OrderedDict
import math
import os
import random
import re
import sys


if __name__ == '__main__':
    s = input()
    chars = Counter(s).items()

    for char, n in sorted(chars, key=lambda c: (-c[1], c[0]))[:3]:
        print(char, n)


##########
# OR
##########
chars = Counter(input()).items()
for char, n in sorted(chars, key=lambda c: (-c[1], c[0]))[:3]:
    print(char, n)

##########
# OR
##########
string = sorted(Counter(input()).items(), key=lambda x: (-x[1], x[0]))[:3]
print("\n".join(x[0] + " " + str(x[1]) for x in string))


##########
# OR
##########
class OrderedCounter(Counter, OrderedDict):
    pass


[print(*c) for c in OrderedCounter(sorted(input())).most_common(3)]
