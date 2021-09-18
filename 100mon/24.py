word = input('文字を入力してください > ')
count = 0

for i in word:
    count += 1

index = count // 2 

if count % 2 == 0:
    word_after = word[:index] + "@" + word[index:]
else:
    word_after = word[:index] + "@" + word[index+1:]
    
print(f"変換した文字 : {word_after}")
