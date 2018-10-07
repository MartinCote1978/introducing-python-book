years_list =[1978, 1979, 1980, 1981, 1982]
age = 0
years_list[age]
last = len(years_list)
years_list[last - 1]


things = ['mozzarella', 'cinderella', 'salmonella']
things[1] = 'CINDERELLA'
things
del(things[2])
things

e2f = {'dog': 'chien', 'cat':'chat', 'walrus':'morse'}
e2f['walrus']
f2e = {v: k for k, v in e2f.items()}
f2e['chien']

e2f.keys()
e2f.values()
