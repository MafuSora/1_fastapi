numbers = [3, 6, 7, 66, 29]
numbers.sort()
sorted(numbers)
print(numbers)

items = [
    ("Product1", 10),
    ("Product2", 20),
    ("Product3", 15),
]


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)
