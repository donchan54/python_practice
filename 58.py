t = (1, [2, 3], '4', (5, 6, 7), None, (9, 10))
t2 = []

for i in t:
    if isinstance(i, tuple):
        t2.append(i)
    elif isinstance(i, list):
        t2.append(tuple(i))
    else:
        t2.append((i, ))
        
print(f"交換したタプル : {t2}")