d = {'B': 222, 'A': 111, 'D': 333, 'C': 444}
d_new = dict(sorted(d.items(), key=lambda x:x[1]))
print(f"Vaueでソートした辞書 : {d_new}")