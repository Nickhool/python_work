__Author__ = "noduez"

import pygal
from die import Die

# 创建一个D6
die_1 = Die()
die_2 = Die()

# 掷几次骰子，并将结果存储在一个列表中
# results = []
# for roll_num in range(1000):
#     result = die_1.roll() + die_2.roll()
#     results.append(result) --- 15-6 使用列表解析代替for循环

results = [die_1.roll() + die_2.roll() for roll_num in range(1000)]

# 分析结果
# frequenies = []
# max_result = die_1.num_sides + die_2.num_sides
# for value in range(2, max_result+1):
#     frequency = results.count(value)
#     frequenies.append(frequency) --- 15-6 使用列表解析替代for循环
max_result = die_1.num_sides + die_2.num_sides
frequenies = [results.count(value) for value in range(2, max_result+1)]

# 对结果进行可视化
hist = pygal.Bar()
hist.title = "Result of rolling two D6 1000 times."
hist.x_labels = [str(x) for x in range(2, max_result + 1)]
hist.y_title = "Frequency of Result"

hist.add('D6 + D6', frequenies)
hist.render_to_file('die_visual_2.svg')