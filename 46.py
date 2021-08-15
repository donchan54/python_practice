l = ['Python 1', 'Java 1', 1, 'Python 2', 'Java 2', 2]
for i in l:
    if 'Python' in str(i):
        l.remove(i)
print(f"文字列'Python'を削除したリスト : {l}")