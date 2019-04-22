import json
import pygal
import math  # 修改的过程中，代码被注释掉了，所以没有用到这个模块

from itertools import groupby

# 将数据加载到一个列表中
filename = 'btc_close_2017.json'
with open(filename) as f:
    btc_data = json.load(f)

dates, months, weeks, weekdays, closes = [], [], [], [], []

# 打印每一天的信息
for btc_dict in btc_data:
    date = btc_dict['date']
    dates.append(date)

    month = int(btc_dict['month'])
    months.append(month)

    week = int(btc_dict['week'])
    weeks.append(week)

    weekday = btc_dict['weekday']
    weekdays.append(weekday)

    close = int(float(btc_dict['close']))
    closes.append(close)

    # print("{} is month {} week {}, {}, the close price is {} RMB".format(date, month, week, weekday, close))


def draw_line(x_data, y_data, title, y_legend):
    """画折线图的函数，传入x轴的数据，y轴数据，标题，说明"""
    xy_map = []
    for x, y in groupby(sorted(zip(x_data, y_data)), key=lambda _: _[0]):
        y_list = [v for _, v in y]
        xy_map.append([x, sum(y_list) / len(y_list)])
    x_unique, y_mean = [*zip(*xy_map)]
    line_chart = pygal.Line()
    line_chart.title = title
    line_chart.x_labels = x_unique
    line_chart.add(y_legend, y_mean)
    line_chart.render_to_file(title + '.svg')
    return line_chart


# # 参数：顺时针旋转20度，不用显示所有x轴标签
# line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
# line_chart.title = '收盘价对数变换 (￥)'
# line_chart.x_labels = dates
# N = 20 # x轴坐标每隔20天显示一次
# line_chart.x_labels_major = dates[::N]
# closes_log = [math.log10(_) for _ in closes]
# line_chart.add('log收盘价', closes_log)
# line_chart.render_to_file("收盘价对数变换折线图 (￥).svg")

# 收盘价月日均值
# 不包括12月这一天
idx_month = dates.index('2017-12-01')
# 实例化
line_chart_month = draw_line(months[:idx_month], closes[:idx_month], '收盘价月日均值 (￥)', '月日均值')
# 调用函数
line_chart_month

# 收盘价周日均值
# 第49周周日是2017-12-10，加1天，因为右不包括
idx_week = dates.index('2017-12-11')
line_chart_week = draw_line(weeks[1:idx_week], closes[1:idx_week], '收盘价周日均值 (￥)', '周日均值')
line_chart_week

# 每周中各天的均值
idx_week = dates.index('2017-12-11')
wd = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# (wd.index(w) + 1)这部分代码加上括号看起来比较清晰
# w对应Monday等，index找出了Monday等的索引，由于索引从0开始，故加1
# 此步骤就将Monday转换成1，其他也对应转换为数字
weekdays_int = [(wd.index(w) + 1) for w in weekdays[1:idx_week]]

line_chart_weekday = draw_line(weekdays_int, closes[1:idx_week], '收盘价星期均值 (￥)', '星期均值')

# 更改了x_labels，并保存为新文件
line_chart_weekday.x_labels = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
line_chart_weekday.render_to_file('收盘价星期均值 (￥) .svg')

with open('收盘价Dashboard.html', 'w', encoding='utf-8') as html_file:
    html_file.write('<html>\n<head>\n<title>收盘价Dashboard</title><meta charset="utf-8"></head>\n<body>\n')
    for svg in [
        '收盘价折线图 (￥).svg',
        '收盘价对数变换折线图 (￥).svg',
        '收盘价月日均值 (￥).svg',
        '收盘价周日均值 (￥).svg',
        '收盘价星期均值 (￥).svg'
    ]:
        html_file.write('   <object type="image/svg+xml" data="{0}" height=500></object>\n'.format(svg))
    html_file.write('</body>\n</html>')