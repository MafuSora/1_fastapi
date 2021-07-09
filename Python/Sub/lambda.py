items = [
    ("Product1", 10),
    ("Product2", 20),
    ("Product3", 15),
]


def sort_item(item):
    return item[1]


items.sort(key=lambda zuzu: zuzu[1])
print(items)
