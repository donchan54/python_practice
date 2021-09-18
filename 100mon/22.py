word1 = input('文字を入力してください > ')
word2 = input('文字を入力してください > ')

r = ""
for i in word1:
    if i in word2 and not i in r:
        r += i
print(f'重複する文字列 : {r}')