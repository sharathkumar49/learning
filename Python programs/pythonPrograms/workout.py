names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heroes = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

print(list(zip(names, heroes)))

my_dict = {}
for name, hero in zip(names, heroes):
	my_dict[name] = hero   # my_dict.update({name: hero})
print(my_dict)
