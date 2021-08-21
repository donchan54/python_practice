d = {'A': 111, 'B': 222, 'C': 333}
l = ['B', 'C', 'D', 'A']

for k in l:
    print(f"{k}に対応するValue : {d.get(k)}")