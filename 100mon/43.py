l = [1, 'aaa', 2, 'bbb', 'ccc', 3, 'ddd', 4]
int_l = sorted([ i for i in l if isinstance(i, int)]) 
str_l = sorted([ i for i in l if isinstance(i, str)])
print(f"ソートしたリスト : {int_l + str_l}")