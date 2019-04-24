
# -*- coding: utf-8 -*-
fplist = ['ash','zofia','glaz']
for name in fplist :
	print('welcome to party! '+name+'!')
print(fplist[2] + '不来了')

#替换元素
fplist[2] = 'fuze'
for name in fplist :
	print('welcome to party! '+name+'!')

#添加元素
fplist.insert(0,'Ying')
print(fplist)
fplist.insert(2,'IQ')
print(fplist)
fplist.append('Ela')
print(fplist)

for name in fplist :
	print('welcome to party! '+name+'!')

print('桌子没到，只能邀请两个人了！')


outp = fplist.pop()
print("I'm so sorry "+ outp)
outp = fplist.pop()
print("I'm so sorry "+ outp)
outp = fplist.pop()
print("I'm so sorry "+ outp)
outp = fplist.pop()
print("I'm so sorry "+ outp)

for name in fplist:
	print( name+' ,You can still come')

del fplist[0]
del fplist[0]
print(fplist)