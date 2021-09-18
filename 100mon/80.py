d = {'B': 222, 'A': 111, 'D': 444, 'C': 333}

d_new = d.copy()

for k,v in d.items():
    if v % 2 == 1:
        del d_new[k]

print(f"奇数を削除した辞書 : {d_new}")