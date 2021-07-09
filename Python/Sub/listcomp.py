items = [
    ("Product1", 10),
    ("Product2", 20),
    ("Product3", 15),
]


prices = [item[1] for item in items]
print(prices)


filtered = [item for item in items if item[1] >= 11]
print(filtered)
