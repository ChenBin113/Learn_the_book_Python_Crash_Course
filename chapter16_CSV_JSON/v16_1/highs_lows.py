import csv
from datetime import datetime

from matplotlib import pyplot as plt

# 从文件中获取日期，最高温和最低温
# filename = "sitka_weather_2014.csv"
filename = "death_valley_2014.csv"
with open(filename) as f:
    reader = csv.reader(f)
    # 先读取了第一行，表头那一行，接下来从第二行开始
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0],"%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    # print(highs)
    # print(lows)

    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.3)

# 设置图形的格式
title = "Daily high and low temperatures - 2014\nDeath Valley, CA"
plt.title(title, fontsize=24)
plt.xlabel('', fontsize=16)
# 绘制斜标签避免重叠问题
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
