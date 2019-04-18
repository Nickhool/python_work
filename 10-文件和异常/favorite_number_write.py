__Author__ = "noduez"

#10-11喜欢的数字
import json

# number = input("What's your favorite number? ")
# with open('favorite_number.json','w') as f_obj:
#     json.dump(number, f_obj)
#     print("Thanks! I'll remember that.")
#
# with open('favorite_number.json', 'r') as f:
#     num = json.load(f)
#     print("I know your favorite number! It's " + str(num) + ".")

# 10-12合二为一
def favorite_number():
    '''记录喜欢的数字'''
    filename = 'favorite_number.json'
    try:
        with open('favorite_number.json', 'r') as f:
            num = json.load(f)

    except FileNotFoundError:
        number = input("What's your favorite number? ")
        with open('favorite_number.json', 'w') as f_obj:
            json.dump(number, f_obj)
            print("Thanks! I'll remember that.")
    else:
        print("I know your favorite number! It's " + str(num) + ".")

favorite_number()
