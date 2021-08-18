d1 = {'A': 111, 'B': 222, 'C': 333}
d2 = {'D': 444, 'E': 555}
d3 = {'F': 666}

d_new = {}

for i in [d1, d2, d3]:
    d_new.update(i)
    
print(f"連結した辞書 : {d_new}")
