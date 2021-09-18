l = [1, '22', 3, '444', 0.0, '5']
l_new = [i for i in l if isinstance(i, int)]
print(f"最大値 : {max(l_new)}")
print(f"最小値 : {min(l_new)}")