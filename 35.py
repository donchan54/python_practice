l = ['1', 2, '3', 4.0, '5', 6, '7', 8.0, '9', 10]

match_list = []

for i in l:
    if isinstance(i, int):
        match_list.append(i)

print(f"整数型に絞り込んだリスト: {match_list}")