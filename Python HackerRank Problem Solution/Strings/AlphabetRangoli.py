import string

alpha = string.ascii_lowercase


def print_rangoli(size):
    # your code goes here
    # print(list(range(size))[::-1] + list(range(1, size)))
    width = 4 * size - 3
    for i in list(range(size))[::-1] + list(range(1, size)):
        print("-".join(alpha[size - 1:i:-1] + alpha[i:size]).center(width, "-"))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
