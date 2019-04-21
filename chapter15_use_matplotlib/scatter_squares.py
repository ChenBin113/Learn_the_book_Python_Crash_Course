#!/usr/bin/env python
# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x ** 2 for x in x_values]

# cmap,Blues,Reds,Greens，删除数据点的轮廓edgecolor
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Greens, edgecolors=None, s=40)

# 设置图表标题，并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)

# 设置坐标轴取值范围
plt.axis([0, 1100, 0, 1100000])
plt.show()
# 自动保存图表，第二个参数：删除多余的空白区域
# 前面如果使用show函数，debug时候程序会暂停，没有运行到这里；用run就可以了
plt.savefig('squares_plot.png',bbox_inches='tight')