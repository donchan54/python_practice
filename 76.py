l = [{'id': 10000, 'feature': {'name': 'Michael', 'height': 180.3, 'weight': 63.7, 'skills': {'IT': ['Python', 'Golang', 'SQL'], 'Others': ['Chinese', 'Math']}}},
    {'id': 10001, 'feature': {'name': 'Nancy', 'height': 156.7, 'weight': 39.7, 'skills': {'IT': ['Java', 'SQL', 'JavaScript'], 'Others': ['Accounting']}}}]

it_skills = [d['feature']['skills']['IT'] for d in l]
michael_skill, nancy_skill = it_skills
common_skill = set(michael_skill) & set(nancy_skill)
print(f'共通するITスキル : {common_skill}')
