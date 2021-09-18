l = ['Python','Ruby','PHP','JavaScript']

min_length_word = l[0]
min_length = len(l[0])

for i in l:
    if len(i) < min_length:
        min_length_word = i
        min_length = len(i)

print(f"一番短い単語 : {min_length_word}")