digits = [1,2,3,4,5,6,7,8,9]

print('The first three items in the list are:')
print(digits[:3])

print('The items from middle of the list are:')
print(digits[3:6])

print('The last three items in the list are:')
print(digits[-3:])


my_pizzas = ['a','b','c']
friend_pizzas = my_pizzas[:]
print('My favorite pizzas are:')
for p in my_pizzas:
	print(p)
print("My friend's favorite pizzas are:")
for p in friend_pizzas:
	print(p)

my_pizzas.append('d')
friend_pizzas.append('e')
print('Actually, my favorite pizzas are:')
for p in my_pizzas:
	print(p)
print("Actually, my friend's favorite pizzas are:")
for p in friend_pizzas:
	print(p)


