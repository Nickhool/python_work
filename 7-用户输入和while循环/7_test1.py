__Author__ = "noduez"

#7-4 披萨配料
prompt = '\nWhat topping would you like on your pizza?'
prompt += "\nEnter 'quit' when you are finished: "
message = ''
while True:
    message = input(prompt)
    if message != 'quit':
        print('We will add '+ message + ' to pizza!')
    else:
        break

#7-5 电影票
prompt = "How old are you?"
prompt += "\nEnter 'quit' when you are finished. "
while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)
    if age < 3:
        print('You get it free!')
    elif age < 13:
        print('Your ticket is $10.')
    else:
        print('Your ticket is $15!')

#7-6
#7-7 无限循环
# x = 1
# while x <= 5:
#     print(x)

