l1 = [1, 2, 3, 4, 5]
l2 = [3, 4, 5]

print(f"l1はl2に含まれる : {set(l1).issubset(set(l2))}")
print(f"l2はl1に含まれる : {set(l2).issubset(set(l1))}")