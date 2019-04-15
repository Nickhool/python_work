# -*- coding: utf-8 -*-
#6-7 字典列表
person0 = {
	'first_name': 'Zhang',
	'last_name': 'xxxdsz',
	'age': 22,
	'city': 'NY',
}
person1 = {
	'first_name': 'He',
	'last_name': 'ere',
	'age': 23,
	'city': 'NY',
}
person2 = {
	'first_name': 'ang',
	'last_name': 'sz',
	'age': 24,
	'city': 'NY',
}
people = [person0,person1,person2]
for person in people:
	print(person)

#6-8 字典列表
pet1 = {
	'type': 1,
	'owner': 'xiaox'
}
pet2 = {
	'type': 4,
	'owner': 'dddds'
}
pet3 = {
	'type': 3,
	'owner': 'zzzz'
}
pets = [pet1,pet2,pet3]
for pet in pets:
	print(pet)

#6-9 在字典中储存列表
favorite_places = {
	'fuze': ['place1','place2','place3'],
	'muke': ['place4','place2'],
	'ela': ['place5'],
}
for name, places in favorite_places.items():
	if len(places) == 1:
		print(name.title() +"'s favorite place is:\n" + places[0])
	else:
		print('\n'+ name.title()+"'s favorite places are:")
		for place in places:
			print(place)
#6-10
favorite_words = {
	'fuze': [3,5,6],
	'blackbreak': [5,9],
	'mira': [1,2,6],
	'buke': [0,7],
	'ela': [7],
}
for name, nums in favorite_words.items():
	if len(nums) == 1:
		print(name.title() +"'s favorite num is:\n" + str(nums[0]))
	else:
		print('\n'+ name.title()+"'s favorite nums are:")
		for num in nums:
			print(num)


#6-11字典中储存字典
cites = {
	'city1': {
		'country': 'aaa',
		'population': '100000',
		'fact': 'aaaaaa'
	},
	'city2': {
		'country': 'bbb',
		'population': '322200000',
		'fact': 'bbbbb'
	},
	'city3': {
		'country': 'ccc',
		'population': '56600000',
		'fact': 'vcccccc'
	}
}
for city,city_info in cites.items():
	print('\ncity: '+city.title())
	print('\tcountry: '+ city_info['country'].title())
	print('\tpopulation: '+ city_info['population'].title())
	print('\tfact: '+ city_info['fact'].title())


