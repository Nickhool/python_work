
# 7-1汽车租赁
message = input('What kind of car do you need: ')
print('Let me see if I can find you a '+ message.title())

# 7-2餐馆订位
num = input('How many people you guys: ')
num = int(num)
if num < 8:
    print('Welcome,please there!')
else:
    print('Sorry, no tables left!')

#7-3 10的整数倍
number = input('please enter a number: ')
number = int(number)
if number % 10 == 0:
    print('The number '+ str(number) + ' is a multiple of 10.')
else:
    print('The number '+ str(number) + ' is not a multiple of 10.')