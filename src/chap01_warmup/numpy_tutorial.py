#!/usr/bin/env python3
# coding: utf-8
# numpy 的 array 操作

# 1. 导入必要的库
import numpy as np  # 导入numpy库并简写为np，用于科学计算
import matplotlib  # 导入matplotlib库，用于绘图
import matplotlib.pyplot as plt  # 导入pyplot模块并简写为plt，用于绘制图表

# 设置matplotlib的后端为TkAgg，确保图形能在窗口中正常显示
matplotlib.use('TkAgg')

# 2. 创建一维数组并输出相关信息
print("第二题：\n")
     
# 创建一个一维数组a，包含元素4,5,6
a = np.array([4, 5, 6])

# (1) 输出数组a的类型
print("(1) 输出 a 的类型（type）\n", type(a))  # 输出：<class 'numpy.ndarray'>
# (2) 输出数组a的形状（维度大小）
print("(2) 输出 a 的各维度的大小（shape）\n", a.shape)  # 输出：(3,)
# (3) 输出数组a的第一个元素
print("(3) 输出 a 的第一个元素（element）\n", a[0])  # 输出：4

# 3. 创建二维数组并输出相关信息
print("第三题：\n")
# 创建一个二维数组b，包含两行三列
b = np.array([[4, 5, 6], [1, 2, 3]])  
# (1) 输出数组b的形状
print("(1) 输出各维度的大小（shape）\n", b.shape)  # 输出：(2,3)
# (2) 输出指定位置的元素
print("(2) 输出 b(0,0)，b(0,1),b(1,1) 这三个元素（对应值分别为 4,5,2）\n", b[0, 0], b[0, 1], b[1, 1])  # 输出：4 5 2

# 4. 创建特殊矩阵
print("第四题：\n")
# (1) 创建3x3的全0矩阵，类型为整型
a = np.zeros((3, 3), dtype=int)
# (2) 创建4x5的全1矩阵
b = np.ones((4, 5))
# (3) 创建4x4的单位矩阵（对角线为1，其余为0）
c = np.eye(4)
# (4) 创建3x2的随机数矩阵（值为0-1之间的随机数）
np.random.seed(42)  # 设置随机种子，确保每次运行结果一致
d = np.random.random((3, 2))

# 5. 创建数组并输出指定元素
print("第五题：\n")
# 创建3x4的二维数组a
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# (1) 打印整个数组
print(a)
# (2) 输出(2,3)和(0,0)位置的元素
print(a[2, 3], a[0, 0])  # 输出：12 1

# 6. 数组切片操作
print("第六题：\n")
# 提取a的第0-1行，第2-3列（注意：切片是左闭右开区间）
b = a[0:2, 2:4]
# (1) 输出切片后的数组b
print("(1) 输出 b\n", b)  # 输出：[[3 4][7 8]]
# (2) 输出b中(0,0)位置的元素
print("(2) 输出 b 的（0,0）这个元素的值\n", b[0, 0])  # 输出：3

# 7. 提取数组最后两行
print("第七题：\n")
# 提取a的最后两行所有列
c = a[-2:, :]  
# (1) 输出切片后的数组c
print("(1) 输出 c \n", c)  # 输出：[[5 6 7 8][9 10 11 12]]
# (2) 输出c中第一行的最后一个元素
print("(2) 输出 c 中第一行的最后一个元素\n", c[0, -1])  # 输出：8

# 8. 高级索引
print("第八题：\n")
# 创建3x2的数组a
a = np.array([[1, 2], [3, 4], [5, 6]])
# 使用列表索引获取(0,0)、(1,1)、(2,0)位置的元素
print("输出:\n", a[[0, 1, 2], [0, 1, 0]])  # 输出：[1 4 5]

# 9. 高级索引应用
print("第九题：\n")
# 创建4x3的数组a
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
# 创建列索引数组b
b = np.array([0, 2, 0, 1])
# 使用高级索引获取(0,0)、(1,2)、(2,0)、(3,1)位置的元素
print("输出:\n", a[np.arange(4), b])  # 输出：[1 6 7 11]

# 10. 通过高级索引修改数组元素
print("第十题：\n")
# 对9题中选中的四个元素各加10
a[np.arange(4), b] += 10
print("输出:", a)  # 输出：[[11 2 3][4 5 16][17 8 9][10 21 12]]

# 11-12. 数组数据类型
print("第十一题：\n")
x = np.array([1, 2])
print("输出:", type(x))  # 输出：<class 'numpy.ndarray'>

print("第十二题：\n")
x = np.array([1.0, 2.0])
print("输出:", type(x))  # 输出：<class 'numpy.ndarray'>

# 13. 数组运算
print("第十三题：\n")
# 创建两个2x2的浮点型数组
x = np.array([[1, 2], [3, 4]], dtype=np.float64)
y = np.array([[5, 6], [7, 8]], dtype=np.float64)
# 两种加法方式
print("x+y\n", x + y)  # 逐元素相加
print("np.add(x,y)\n", np.add(x, y))  # 同上

# 14. 数组减法
print("第十四题：\n")
print("x-y\n", x - y)  # 逐元素相减
print("np.subtract(x,y)\n", np.subtract(x, y))  # 同上

# 15. 数组乘法比较
print("第十五题：\n")
print("x*y\n", x * y)  # 逐元素相乘
print("np.multiply(x, y)\n", np.multiply(x, y))  # 同上
print("np.dot(x,y)\n", np.dot(x, y))  # 矩阵乘法（行乘列）

# 16. 数组除法
print("第十六题：\n")
print("x/y\n", x / y)  # 逐元素相除
print("np.divide(x,y)\n", np.divide(x, y))  # 同上

# 17. 数组开方
print("第十七题：\n")
print("np.sqrt(x)\n", np.sqrt(x))  # 对每个元素开平方

# 18. 矩阵乘法
print("第十八题：\n")
print("x.dot(y)\n", x.dot(y))  # 矩阵乘法
print("np.dot(x,y)\n", np.dot(x, y))  # 同上

# 19. 数组求和
print("第十九题：\n")
print("print(np.sum(x)):", np.sum(x))  # 所有元素求和
print("print(np.sum(x, axis=0))", np.sum(x, axis=0))  # 按列求和
print("print(np.sum(x, axis=1))", np.sum(x, axis=1))  # 按行求和

# 20. 数组求平均
print("第二十题：\n")
print("print(np.mean(x))", np.mean(x))  # 全局平均
print("print(np.mean(x,axis = 0))", np.mean(x, axis=0))  # 列平均
print("print(np.mean(x,axis = 1))", np.mean(x, axis=1))  # 行平均

# 21. 矩阵转置
print("第二十一题：\n")
print("x 转置后的结果:\n", x.T)  # 行列互换

# 22. 指数运算
print("第二十二题：\n")
print("e 的指数：np.exp(x)")  
print(np.exp(x))  # 对每个元素求e的指数

# 23. 最大值索引
print("第二十三题：\n")
print("全局最大值的下标:", np.argmax(x))  # 整个数组中最大值的索引
print("每列最大值的下标:", np.argmax(x, axis=0))  # 每列最大值的索引
print("每行最大值的下标:", np.argmax(x, axis=1))  # 每行最大值的索引

# 24. 绘制二次函数图像
print("第二十四题：\n")
# 生成x值（0到100，步长0.1）
x = np.arange(0, 100, 0.1)
# 计算y=x^2
y = x * x

# 创建图形窗口
plt.figure(figsize=(10, 6))
# 绘制曲线
plt.plot(x, y, label="y = x^2", color="blue")
# 添加标题和标签
plt.title("Plot of y = x^2")
plt.xlabel("x")
plt.ylabel("y")
# 添加网格和图例
plt.grid(True, alpha=0.5)
plt.legend(loc='upper right')
# 显示图形
plt.show()

# 25. 绘制正弦和余弦函数
print("第二十五题：\n")
# 生成x值（0到3π，步长0.1）
x = np.arange(0, 3 * np.pi, 0.1)
# 计算正弦和余弦值
y_sin = np.sin(x)
y_cos = np.cos(x)

# 创建图形窗口
plt.figure(figsize=(10, 6))
# 绘制两条曲线
plt.plot(x, y_sin, label="y = sin(x)", color="blue")
plt.plot(x, y_cos, label="y = cos(x)", color="red")
# 添加标题和标签
plt.title("Sine and Cosine Functions")
plt.xlabel("x")
plt.ylabel("y")
# 添加网格和图例
plt.grid(True)
plt.legend()
# 显示图形
plt.show()
