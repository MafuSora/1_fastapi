items = [
    ("Product1", 10),
    ("Product2", 20),
    ("Product3", 15),
]

harga = map(lambda item: item[1], items)
for item in harga:
    print(item)

filtered = []

for item in items:
    if item[1] > 10:
        filtered.append(item)

print(*filtered)

x = filter(lambda item: item[1] > 10, items)
for item in x:
    print(item)
