word1 = input('文字を入力してください > ')
word2 = input('文字を入力してください > ')
word3 = input('文字を入力してください > ')

words = [word1, word2, word3]

words.sort()
sort_words = ' , '.join(words)
print(f"並び替えた英単語 : {sort_words}")