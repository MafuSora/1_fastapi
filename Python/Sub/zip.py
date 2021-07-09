list1 = [1, 2, 3]
list2 = [10, 20, 30]

x = zip(list1, list2)
for item in x:
    print(item)

y = zip("abc", list1, list2)
for item in y:
    print(item)
