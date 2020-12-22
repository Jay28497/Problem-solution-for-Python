for t in range(input()):
    input()
    lst = map(int, raw_input().split())
    l = len(lst)
    i = 0
    while i < l - 1 and lst[i] >= lst[i + 1]:
        i += 1
    while i < l - 1 and lst[i] <= lst[i + 1]:
        i += 1
    print("Yes" if i == l - 1 else "No")

##########
# OR
##########
for t in range(int(input())):
    input()
    lst = [int(i) for i in input().split()]
    min_list = lst.index(min(lst))
    left = lst[:min_list]
    right = lst[min_list+1:]
    if left == sorted(left, reverse=True) and right == sorted(right):
        print("Yes")
    else:
        print("No")
