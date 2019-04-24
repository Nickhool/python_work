# -*- coding: utf-8 -*-

#6-4 词汇表2
learned_words = {
	'Int': 'Python可以处理任意大小的整数，当然包括负整数，在程序中的表示方法和数学上的写法一模一样，例如：1，100，-8080，0，等等。',
	'Float': '浮点数也就是小数，之所以称为浮点数，是因为按照科学记数法表示时，一个浮点数的小数点位置是可变的。',
	'Str': '字符串是以单引号或双引号括起来的任意文本。',
	'Slice': '取一个list或tuple的部分元素是非常常见的操作，对这种经常取指定索引范围的操作，用循环十分繁琐，因此，Python提供了切片（Slice）操作符，能大大简化这种操作。',
	'Iteration': '如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）',
	'List Comprehensions': '列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。',
	'generator': '在Python中，这种一边循环一边计算的机制，称为生成器：generator',
	'Iterator': '可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。',
}
for k,v in learned_words.items():
	print(k + ': ' + v)

#6-5 河流
rivers = {
	'mississippi': 'america',
	'amazon': 'brazil',
	'volga': 'Russia',
}
print('\n6-5')
for k,v in rivers.items():
	print('The ' + k.title() + 'run through ' + v.title() )
for river_name in rivers.keys():
	print(river_name)
for country_name in rivers.values():
	print(country_name)

#6-6
print('\n6-6调查')
favorite_languages = {
	'fuze': 'python',
	'smoke': 'ruby',
	'mira': 'c',
	'buke': 'java'
}
poll_people = ['ela','mozi','zofia','fuze','mira']
polled_people = []
for name in favorite_languages.keys():
	polled_people.append(name)
for name in poll_people:
	if name in polled_people:
		print('Hi' + name.title() +
			', I see your favorite language is ' +
			favorite_languages[name].title() + '!')
	else:
		print(name.title()+', please take our poll!')