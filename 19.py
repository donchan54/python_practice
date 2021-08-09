word = input('文字を入力してください > ')
vowels = ['a', 'i', 'u', 'e', 'o']
new_word = ""

for i in word:
    if i in vowels:
        continue
    new_word += i

print(f"作成した文字 : {new_word}")