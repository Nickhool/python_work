# -*- coding: utf-8 -*-
#判断字符串相等
stra = 'aaaa'

print("Is stra == 'aaaa'? I predict True.")
print(stra == "aaaa")
print("Is stra == 'bbbb'? I predict False.")
print(stra == 'bbbb')

#lower
print('\n关于lower()---')
str1 = 'Audi'
str2 = 'audi'
print(str1 == str2)
print(str1.lower() == str2)

# 大小于和 and or
print('\n大小于和 and or')
num1 = 1
num2 = 2
num3 = 3
print(num1<5 and num2<5)
print(num1>5 or num2>5)


#in 和 not i
print('\nin 和 not i')
nums = [1, 2, 3, 4, 5]
print(1 in nums)
print(5 not in nums)