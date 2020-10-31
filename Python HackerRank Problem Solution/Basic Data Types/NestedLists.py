if __name__ == '__main__':

    list1 = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list1.append([name, score])

    second_highest = sorted(list(set([marks for name, marks in list1])))[1]
    print('\n'.join([a for a, b in sorted(list1) if b == second_highest]))
