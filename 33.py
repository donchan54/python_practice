l1 = ['Python', 'Ruby', 'PHP', 'JavaScript']
l2 = ['Java', 'Ruby', 'Golang', 'Python', 'TypeScript'] 

match_list = []

for i in l1:
    for l in l2:
        if i == l:
            match_list.append(i)
            
print(f"共通する値を格納したリスト: {match_list}")