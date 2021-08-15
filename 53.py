l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l_new = [tuple(l[i:i+3]) for i in range(0, 9, 3)]
print(f'3分割したタプル : {l_new}')