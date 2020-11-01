list1 = [10, 20, 4, 45, 99]
mx = max(list1[0], list1[1])
secondMax = min(list1[0], list1[1])
n = len(list1)
for i in range(2, n):
    if list1[i] > mx:
        secondMax = mx
        mx = list1[i]
    elif secondMax < list1[i] != mx:
        secondMax = list1[i]

print("Second highest number is : ", str(secondMax))


###########################################################
def second_largest(numbers):
    count = 0
    m1 = m2 = float('-inf')
    for x in numbers:
        count += 1
        if x > m2:
            if x >= m1:
                m1, m2 = x, m1
            else:
                m2 = x
    return m2 if count >= 2 else None


l1 = [1, 2, 3, 4, 5, 6]
print(second_largest(l1))

###########################################################
numbers = [20, 67, 3, 2.6, 7, 74, 2.8, 90.8, 52.8, 4, 3, 2, 5, 7]
if numbers[0] > numbers[1]:
    m, m2 = numbers[0], numbers[1]
else:
    m, m2 = numbers[1], numbers[0]

for x in numbers[2:]:
    if x > m2:
        if x > m:
            m2, m = m, x
        else:
            m2 = x
print(m2)
