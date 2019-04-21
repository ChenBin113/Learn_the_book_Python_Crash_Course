# 项目总体使用环境
- Windows 10
- pycharm 2019.1
- anaconda管理
- Python 3.6

# 飞机大战外星人
- import pygame
	
## 【安装pygame包】
    - 用anaconda的指令栏安装
    - 先创建好虚拟环境（或者激活已有环境，确保不会污染其他的编程环境）
    - 再用pip指令安装
    - 先用pip list检查安装包是否存在
    - 然后用pip install pygame（包名称，此处用pygame）安装
    - 通过安装之后发现，就算先激活conda环境，也只是将安装包先安装到anaconda总环境下，如果没有激活，则是安装到电脑的python中，在需要使用包的时候点击pycharm中setting的anaconda图标刷新后就可以手动添加包了
    - 之后在pycharm中就可以手动添加pygame包
    - 安装其他包也可以使用这个流程
		
- 增加setting模块，将设置统一划分到一个类中，达到分类的目的
- 代码重构，使结构更清晰，更简洁
- 在这个项目中，每个元素都以rect为参考，简化了模型的边界

# 数据可视化
- matplotlib库的安装
	- [解决pycharm中matplotlib、plt.show()画图时报错“qt platform问题”](https://blog.csdn.net/tudianlu9350/article/details/79695372)