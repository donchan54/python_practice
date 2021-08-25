l = [1, 0, [], (2, 3), 'AA', '', False, ''*3]

l_new = sum([bool(i) for i in l])
print(f"Trueの数 : {l_new}")