# >>> from collections import OrderedDict
# >>>
# >>> ordinary_dictionary = {}
# >>> ordinary_dictionary['a'] = 1
# >>> ordinary_dictionary['b'] = 2
# >>> ordinary_dictionary['c'] = 3
# >>> ordinary_dictionary['d'] = 4
# >>> ordinary_dictionary['e'] = 5
# >>>
# >>> print ordinary_dictionary
# {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4}
# >>>
# >>> ordered_dictionary = OrderedDict()
# >>> ordered_dictionary['a'] = 1
# >>> ordered_dictionary['b'] = 2
# >>> ordered_dictionary['c'] = 3
# >>> ordered_dictionary['d'] = 4
# >>> ordered_dictionary['e'] = 5
# >>>
# >>> print ordered_dictionary
# OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)])


# Sample Input
#
# 9
# BANANA FRIES 12
# POTATO CHIPS 30
# APPLE JUICE 10
# CANDY 5
# APPLE JUICE 10
# CANDY 5
# CANDY 5
# CANDY 5
# POTATO CHIPS 30


# Sample Output
#
# BANANA FRIES 12
# POTATO CHIPS 60
# APPLE JUICE 20
# CANDY 20


from collections import OrderedDict

d = OrderedDict()
for _ in range(int(input())):
    item, space, quantity = input().rpartition(' ')
    d[item] = d.get(item, 0) + int(quantity)
for item, quantity in d.items():
    print(item, quantity)
