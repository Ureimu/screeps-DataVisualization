import json
import matplotlib.pyplot as plt
import matplotlib
scMemP = open(r"memory.json", "r", encoding="utf-8")
scMem = json.loads(scMemP.readline())
print(scMem)
stats = scMem['data']
print(stats['gcl'])
# 1 基础绘图
# 第1步：定义x和y坐标轴上的点   x坐标轴上点的数值
x = [1, 2, 3, 4]
# y坐标轴上点的数值
y = [1, 4, 9, 16]
# 第2步：使用plot绘制线条第1个参数是x的坐标值，第2个参数是y的坐标值
plt.plot(x, y)
# 第3步：显示图形
plt.show()

# 2 定义绘图属性
'''
color：线条颜色，值r表示红色（red）
marker：点的形状，值o表示点为圆圈标记（circle marker）
linestyle：线条的形状，值dashed表示用虚线连接各点
'''
plt.plot(x, y, color='r', marker='o', linestyle='dashed')
# plt.plot(x, y, 'ro')
'''
axis：坐标轴范围
语法为axis[xmin, xmax, ymin, ymax]，
也就是axis[x轴最小值, x轴最大值, y轴最小值, y轴最大值]
'''
plt.axis([0, 6, 0, 20])
plt.show()

# 3 给图片提阿甲注释和标题等

# 第1步：定义x和y坐标轴上的点  x坐标轴上点的数值
x = [1, 2, 3, 4]
# y坐标轴上点的数值
y = [1, 4, 9, 16]

# 第2步：使用plot绘制线条 第1个参数是x的坐标值，第2个参数是y的坐标值
plt.plot(x, y)
# 添加文本 设置字体
# x轴文本
plt.xlabel(u'x坐标轴')
# y轴文本
plt.ylabel(u'y坐标轴')
# 标题
plt.title(u'标题')
# 添加注释 参数名xy：箭头注释中箭头所在位置，参数名xytext：注释文本所在位置，
# arrowprops在xy和xytext之间绘制箭头, shrink表示注释点与注释文本之间的图标距离

plt.annotate(u'我是注释', xy=(2, 5), xytext=(2, 10),
             arrowprops=dict(facecolor='black', shrink=0.01),
             )

# 第3步：显示图形
plt.show()
