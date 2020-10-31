if __name__ == '__main__':
    N = int(input())
    l = []

    for i in range(N):
        # print("N -->>",i)
        res = input().split()
        # print("res -->>",res)
        # print("res[0], append -->>",res[0], "append")
        if res[0] == "append":
            l.append(int(res[1]))
        elif res[0] == "insert":
            l.insert(int(res[1]), int(res[2]))
        elif res[0] == "remove":
            l.remove(int(res[1]))
        elif res[0] == "pop":
            l.pop()
        elif res[0] == "sort":
            l.sort()
        elif res[0] == "reverse":
            l.reverse()
        elif res[0] == "print":
            print(l)
