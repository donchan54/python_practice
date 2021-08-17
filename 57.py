t = (1, [2, 3], '4', (5, 6, 7), '8', (9, 10))
t2 = [i for i in t if isinstance(i, tuple)]
print(f"タプルに含まれるタプルの数 : {len(t2)}")