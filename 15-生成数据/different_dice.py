__Author__ = "noduez"

from die import Die

import pygal

# 创建一个D6和一个D10
die_1 = Die()
die_2 = Die(10)

# 掷几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# 分析结果
frequenies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequenies.append(frequency)

# 对结果进行可视化
hist = pygal.Bar()
hist.title = 'Result of rolling D6&D10 50000 times.'
hist.x_labels = [str(x) for x in range(2, max_result + 1)]
hist.y_title = 'Frequency of Result'

hist.add('D6 + D10', frequenies)
hist.render_to_file('die_visual_3.svg')
# hist.render()