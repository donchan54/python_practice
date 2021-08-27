s = 'This is the Python exercise.'
l = [v for v in s.split() if 't' not in v]

new_s = ' '.join(l)
print(f'削除後の文字列 : {new_s}')
