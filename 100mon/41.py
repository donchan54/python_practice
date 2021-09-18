l = [0, '1', 3, 2, '4', 5, '7']
l_new = [v for i,v in enumerate(l) if i == int(v)]
print(f'インデックスと値が一致 : {l_new}')
