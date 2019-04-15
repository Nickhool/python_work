# -*- coding: utf-8 -*-

#6-1
person_dict = {
	'first_name': 'Zhang',
	'last_name': 'xxxdsz',
	'age': 22,
	'city': 'NY',
}
print(person_dict['first_name'])
print(person_dict['last_name'])
print(person_dict['age'])
print(person_dict['city'])

#6-2
favorite_words = {
	'fuze': 3,
	'blackbreak': 5,
	'mira': 6,
	'buke': 1,
	'ela': 7,
}
print(favorite_words)

#6-3
learned_words = {
	'Int': 'Python可以处理任意大小的整数，当然包括负整数，在程序中的表示方法和数学上的写法一模一样，例如：1，100，-8080，0，等等。',
	'Float': '浮点数也就是小数，之所以称为浮点数，是因为按照科学记数法表示时，一个浮点数的小数点位置是可变的。',
	'Str': '字符串是以单引号或双引号括起来的任意文本。',
}
print('整数: '+learned_words['Int'])
print('浮点数: '+learned_words['Float'])
print('字符串: '+learned_words['Str'])
print(learned_words['Int'].decode('utf-8'))
