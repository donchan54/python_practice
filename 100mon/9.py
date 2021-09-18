d = {}
for i in range(1,31):
    if i % 3 == 0:
        index = f"{i // 3}番目"
        d[index] = i
print(f"作成したリスト:{d}")