l = [1, 2, 3, 4, 5]

if any(isinstance(i, str) for i in l):
    print("文字列が入ってます")
else:
    print("文字列は入っていません")