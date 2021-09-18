l = [1, 2, None, False, '3', '4', None, True]

l_new = len([i for i in l if i is True or i is None])
print(f"TrueとNoneの数 : {l_new}")