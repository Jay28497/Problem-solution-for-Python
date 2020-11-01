def minimum(list):
    res = list[0]
    for x in list[0:]:
        if x < res:
            res = x
    return res


list1 = [10, 20, 4, 105, 99]
print("Largest element is:", minimum(list1))
