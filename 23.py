sentence1 = input('英文を入力してください > ')
sentence2 = input('英文を入力してください > ')

sentence1 = sentence1.split()
sentence2 = sentence2.split()

r = []
for i in sentence1:
    if i in sentence2 and not i in r:
        r.append(i)
print(f'重複する英単語 : {r}')