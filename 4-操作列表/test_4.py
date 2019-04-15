# 1~20
# for value in range(1,21):
# 	print(value)

# 1~1000000
# for i in list(range(1,1000001)):
# 	print(i)

# million = list(range(1,1000001))
# print(min(million))
# print(max(million))
# print(sum(million))

# for v in range(1,20,2):
# 	print(v)

# for v in range(3,30,3):
# 	print(v)

# 立方
cubes1 = []
for v in range(1,10):
	cubes1.append(v**3)
for v in cubes1:
	print(v)

# 立方解析
cubes = [v**3 for v in range(1,10)]
for v in cubes:
	print(v)
