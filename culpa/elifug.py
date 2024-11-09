import functools
items = ['a', 'b', 'c']
sep = '-'
result = functools.reduce(lambda x, y: x + sep + y, items)
print(result)  # Output: 'a-b-c'
