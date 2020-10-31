def average(array):
    # your code goes here
    l = len(set(array))
    s = set(array)
    sum = 0
    for i in s:
        sum += int(i)
    return sum / l


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
