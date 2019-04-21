import pygal
from dice import Dice

# 创建一个6面和一个10面骰子
dice_1 = Dice()
dice_2 = Dice(10)

results = []
for roll_num in range(50000):
    result = dice_1.roll() + dice_2.roll()
    results.append(result)

# 分析结果
frequencies = []
max_resulut = dice_1.num_sides + dice_2.num_sides
for value in range(2, max_resulut + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化
hist = pygal.Bar()

hist.title = "Results of rolling a D6 and a D10 50,000 times."
# D6和D10，循环生成labels
hist_temp = []
for i in range(2, dice_1.num_sides + dice_2.num_sides + 1):
    hist_temp.append(str(i))
hist.x_labels = hist_temp
# hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D10', frequencies)
hist.render_to_file('dice_visual.svg')

print(frequencies)
