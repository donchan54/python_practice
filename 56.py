t = (1, '2', 3, '4', 5)
str_t = (str(i) for i in t)
print(f"str型 : {str_t}")

converted_int = int(''.join(str_t))
print(f'変換後の数値 : {converted_int}')