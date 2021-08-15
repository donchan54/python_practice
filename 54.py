l = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

for i, row in enumerate(l, start=1):
    a, b, c = row
    print(f"{i}行目の値 : {a} {b} {c}")