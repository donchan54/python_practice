word = input('文字を入力してください > ')

if word[0].islower():
    word_after = word.upper()
    print(f"変換後の文字列 : {word_after}")
elif word[0].isupper():
    print(f"変換後の文字列 : {word*2}")
else:
    print("先頭は小文字か大文字を入力してください。")