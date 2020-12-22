# from collections import defaultdict
# d = defaultdict(list)
# d['python'].append("awesome")
# d['something-else'].append("not relevant")
# d['python'].append("language")
# for i in d.items():
#     print i
#
# print:
# ('python', ['awesome', 'language'])
# ('something-else', ['not relevant'])


from collections import defaultdict

n, m = map(int, input().split())
d = defaultdict(list)

for i in range(1, n + 1):
    d[input()].append(str(i))

for i in range(m):
    print(' '.join(d[input()]) or -1)
