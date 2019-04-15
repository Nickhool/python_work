# -*- coding: utf-8 -*-
#5-3
alien_color = 'green'
if alien_color == 'green':
	print('You get 5 point!\n')

alien_color = 'yellow'
if alien_color == 'green':
	print('You get 5 point!')


#5-4
alien_color = 'green'
if alien_color == 'green':
	print('You get 5 point!')
else:
	print('You get 10 point!')

alien_color = 'yellow'
if alien_color == 'green':
	print('You get 5 point!')
else:
	print('You get 10 point!\n')

#5-5
alien_color = 'red'
if alien_color == 'green':
	print('You get 5 point!')
elif alien_color == 'yellow':
	print('You get 10 point!')
else:
	print('You get 15 point!')

alien_color = 'yellow'
if alien_color == 'green':
	print('You get 5 point!')
elif alien_color == 'yellow':
	print('You get 10 point!')
else:
	print('You get 15 point!')

alien_color = 'green'
if alien_color == 'green':
	print('You get 5 point!\n')
elif alien_color == 'yellow':
	print('You get 10 point!')
else:
	print('You get 15 point!')


#5-6
age = 88
if age < 2:
	print('he is a baby')
elif age < 4:
	print('he is learning walk')
elif age < 13:
	print('he is a kid')
elif age < 20:
	print('he is a teenager')
elif age < 65:
	print('he is a adult')
else: 
	print('old man!\n')

#5-7
favorite_fruits = ['orange','mango','pineapple','tomato','bananas']
if 'orange' in favorite_fruits:
	print('You really like orange!')
if 'mango' in favorite_fruits:
	print('You really like mango!')
if 'pineapple' in favorite_fruits:
	print('You really like pineapple!')
if 'tomato' in favorite_fruits:
	print('You really like tomato!')
if 'bananas' in favorite_fruits:
	print('You really like bananas!\n')

#5-8
users = ['admin','Fuze','Ela','Ash','IQ']
if users:
	for user in users:
		if user == 'admin':
			print('hello '+ user +', would you like to see a status report?')
		else: 
			print('hello '+ user +', thank you for logging again')
else:
	print('We need to find some users!')

#5-10 - 检查用户名(不分大小写)
print('\n5-10')
current_users = ['admin','Fuze','Ela','ash','IQ']
new_users = ['Admin','glaz','smoke','mozi','Fuze']
current_users_lower = []
for current_user in current_users:
	current_users_lower.append(current_user.lower())
print(current_users_lower)

for new_user in new_users:
	if new_user.lower() in current_users_lower:
		print(new_user+' has been used, try others!')
	else:
		print('You can use '+ new_user)

#5-11 序数
numbers = [1,2,3,4,5,6,7,8,9]
for number in numbers:
	if number == 1:
		print(str(number)+'st')
	if number == 2:
		print(str(number)+'nd')
	if number == 3:
		print(str(number)+'rd')
	if number == 4:
		print(str(number)+'th')
	if number == 5:
		print(str(number)+'th')
	if number == 6:
		print(str(number)+'th')
	if number == 7:
		print(str(number)+'th')
	if number == 8:
		print(str(number)+'th')
	if number == 9:
		print(str(number)+'th')


