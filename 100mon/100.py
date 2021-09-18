methods = dir(list)
non_special_methods = [s for s in methods if not '__' in s]
print('リストで使えるメソッド一覧：')
print(non_special_methods)
