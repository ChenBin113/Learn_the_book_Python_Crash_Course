import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)

# 状态码，看服务器对请求的回应是什么
print("Status code:", r.status_code)

# 将API响应存储在一个变量中，因为信息是JSON格式，用json方法存储在一个字典中
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])

# 研究有关仓库的信息
repo_dicts = response_dict['items']
print("Number of items:", len(repo_dicts))

names, plot_dicts = [], []

# 研究第一个仓库
# repo_dict = repo_dicts[0]

# print("\nKeys:", len(repo_dict))
# for key in sorted(repo_dict.keys()):
#     print(key)

# 处理结果
# print(response_dict.keys())
# print(response_dict['incomplete_results'])
# print("\nSelected information about first repository:")
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': repo_dict['description'],
        'xlink': repo_dict['html_url'],
    }
    plot_dicts.append(plot_dict)
    # stars.append(repo_dict['stargazers_count'])
    # print("Name:", repo_dict['name'])
    # print("Owner:", repo_dict['owner']['login'])
    # print("Stars:", repo_dict['stargazers_count'])
    # print("Repository:", repo_dict['html_url'])
    # print("Created:", repo_dict['created_at'])
    # print("Updated:", repo_dict['updated_at'])
    # print("Description:", repo_dict['description'])

# 可视化
# 深蓝色，LS类，
my_style = LS('#333366', base_style=LCS)

# 创建实例
my_config = pygal.Config()
# 顺时针转动45度
my_config.x_label_rotation = 45
# 隐藏图例
my_config.show_legend = False
# 标题字体，标签字体，主要标签字体
my_config.title_font_size = 24
my_config.label_font_size = 14

# 这一句暂时没有起到作用
my_config.major_label_font_size = 24

# 较长的项目名称缩短到15个字符
my_config.truncate_label = 15
# 隐藏图中的水平线
my_config.show_y_guides = False
my_config.width = 1000
# my_config.x_labels_major_every = 20000

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names

chart.add('', plot_dicts)

# 最后这一行和书上不一样，需要decode解码
chart.render_to_file('python_repos.svg', decode='utf-8')