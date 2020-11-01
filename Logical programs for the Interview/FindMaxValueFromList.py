def myMax(list):
    res = list[0]
    for x in list:
        if x > res:
            res = x
    return res


list1 = [10, 20, 4, 105, 99]
print("Largest element is:", myMax(list1))
