__Author__ = "noduez"

#8-12 三明治
def make_sandwich(*items):
    '''概述要制作的三明治'''
    print("\nI'll make you a great sandwich:")
    for item in items:
        print("  ...adding " + item + " to your sandwich.")
    print("Your sandwich is ready!")
make_sandwich('roast beef', 'cheddar cheese', 'lettuce', 'honey dijon')
make_sandwich('turkey', 'apple slices', 'honey mustard')
make_sandwich('peanut butter', 'strawberry jam')

#8-13 用户简介
def build_profile(first,last,**user_info):
    '''创建一个字典，其中包含我们知道的关于用户的一切信息'''
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for k,v in user_info.items():
        profile[k] = v
    return  profile
user_profile = build_profile('Zhang','sj',
                             location='sjz',
                             field='IT',
                             sex='man')
print(user_profile)

#8-14 汽车
def make_car(name, type, **car_info):
    profile = {}
    profile['name'] = name
    profile['type'] = type
    for k,v in car_info.items():
        profile[k] = v
    return profile
car_profile = make_car('audi','ccc',color='red',two_package=True,year=1998)
print(car_profile)