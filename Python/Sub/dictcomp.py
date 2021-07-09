values = []
for x in range(10):
    values.append(x*2)
print(values)


total = [x*2 for x in range(5)]
print(total)

kali = {x: x*2 for x in range(5)}
for x, y in kali.items():
    print(f"{x} dikali dengan 2 = {y}")
