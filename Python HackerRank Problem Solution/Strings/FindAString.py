def count_substring(string, sub_string):
    count = 0
    while sub_string in string:
        count += 1
        # print(string.find(sub_string))
        string = string[string.find(sub_string) + 1:]
        # print(string)
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
