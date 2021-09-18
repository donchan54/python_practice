word = input('文字を入力してください > ')

d = {}
for i in word:
    if i in d.keys():
        d[i] += 1
    else:
        d[i] = 1
print(d)