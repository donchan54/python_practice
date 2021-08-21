from typing import ValuesView


d = {'A': 111, 'B': 222, 'C': 333}

d_new = {k:v for k, v in d.items() if v > 150}
print(f"絞り込みをかけた辞書 : {d_new}")