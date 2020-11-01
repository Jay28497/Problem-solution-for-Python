def bubbleSort(list):
    for num in range(len(list) - 1, 0, -1):
        for i in range(num):
            if list[i] > list[i + 1]:
                temp = list[i]
                list[i] = list[i + 1]
                list[i + 1] = temp


list = [12, 5, 43, 28, 95, 41, 45, 23, 74]
bubbleSort(list)
print(list)
