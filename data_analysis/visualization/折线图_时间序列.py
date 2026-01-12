"""
折线图 - 时间序列分析
适用于C题：展示数据随时间变化的趋势，对比预测值与真实值
"""

import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta

# ==================== 设置中文字体 ====================
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']  # Mac系统
# plt.rcParams['font.sans-serif'] = ['SimHei']  # Windows系统
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# ==================== 生成示例数据 ====================
# 生成时间序列（这里填入你的时间数据）
start_date = datetime(2023, 1, 1)
dates = [start_date + timedelta(days=i) for i in range(100)]  # 100天的数据
x = np.arange(100)  # 数值型x轴（如果用日期，使用dates）

# 生成模拟数据（这里替换成你的真实数据）
y_true = 50 + 10 * np.sin(x / 10) + np.random.normal(0, 2, 100)  # 真实值
y_pred = 50 + 10 * np.sin(x / 10)  # 预测值

# 如果有多个数据系列（这里填入你的多组数据）
y_model1 = 50 + 10 * np.sin(x / 10) + 1
y_model2 = 50 + 10 * np.sin(x / 10) - 1

# ==================== 创建图表 ====================
fig, ax = plt.subplots(figsize=(12, 6), dpi=300)

# 绘制真实值（蓝色实线）
ax.plot(x, y_true, 
        color='#2E86AB',  # 颜色（这里可以改成其他颜色，如 'red', 'blue', '#FF5733'）
        linewidth=2,  # 线条粗细
        marker='o',  # 标记点样式（'o'圆点, 's'方块, '^'三角, 'D'菱形, None不显示）
        markersize=3,  # 标记点大小
        label='真实值',  # 图例标签（这里填入你的数据名称）
        alpha=0.8)  # 透明度（0-1，1为不透明）

# 绘制预测值（红色虚线）
ax.plot(x, y_pred,
        color='#F18F01',
        linewidth=2.5,
        linestyle='--',  # 线型（'-'实线, '--'虚线, '-.'点划线, ':'点线）
        label='预测值',
        alpha=0.9)

# 绘制其他模型对比（可选）
ax.plot(x, y_model1, color='#6A994E', linewidth=2, linestyle='-.', label='模型1', alpha=0.7)
ax.plot(x, y_model2, color='#BC4B51', linewidth=2, linestyle=':', label='模型2', alpha=0.7)

# ==================== 添加置信区间（O奖加分项！）====================
# 计算置信区间（这里使用±2标准差作为示例）
confidence_lower = y_pred - 3  # 置信区间下界（这里填入你计算的下界）
confidence_upper = y_pred + 3  # 置信区间上界（这里填入你计算的上界）

# 绘制置信区间阴影
ax.fill_between(x, confidence_lower, confidence_upper,
                color='#F18F01',  # 阴影颜色
                alpha=0.2,  # 透明度（建议0.1-0.3）
                label='95%置信区间')  # 图例标签

# ==================== 标注关键点 ====================
# 找出最大值和最小值的位置
max_idx = np.argmax(y_true)
min_idx = np.argmin(y_true)

# 标注最大值
ax.annotate(f'峰值: {y_true[max_idx]:.2f}',  # 标注文本（这里可以改成你想显示的内容）
            xy=(x[max_idx], y_true[max_idx]),  # 标注点的位置
            xytext=(10, 10),  # 文本偏移量（x偏移, y偏移）
            textcoords='offset points',
            fontsize=10,
            bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', alpha=0.7),  # 文本框样式
            arrowprops=dict(arrowstyle='->', color='red', lw=1.5))  # 箭头样式

# 标注最小值
ax.annotate(f'谷值: {y_true[min_idx]:.2f}',
            xy=(x[min_idx], y_true[min_idx]),
            xytext=(10, -20),
            textcoords='offset points',
            fontsize=10,
            bbox=dict(boxstyle='round,pad=0.5', facecolor='lightblue', alpha=0.7),
            arrowprops=dict(arrowstyle='->', color='blue', lw=1.5))

# ==================== 设置坐标轴和标题 ====================
ax.set_xlabel('时间 (天)', fontsize=12, fontweight='bold')  # x轴标签（这里填入你的x轴名称）
ax.set_ylabel('数值', fontsize=12, fontweight='bold')  # y轴标签（这里填入你的y轴名称）
ax.set_title('时间序列预测分析', fontsize=14, fontweight='bold', pad=20)  # 图表标题（这里填入你的标题）

# ==================== 设置图例 ====================
ax.legend(loc='upper right',  # 图例位置（'upper right', 'upper left', 'lower right', 'lower left', 'best'）
          frameon=True,  # 是否显示图例边框
          shadow=True,  # 是否显示阴影
          fontsize=10)  # 图例字体大小

# ==================== 设置网格 ====================
ax.grid(True,  # 是否显示网格
        alpha=0.3,  # 网格透明度
        linestyle='--',  # 网格线型
        linewidth=0.5)  # 网格线宽

# ==================== 保存和显示图表 ====================
plt.tight_layout()  # 自动调整布局
plt.savefig('折线图_时间序列.png', dpi=300, bbox_inches='tight')  # 保存图片（这里改成你想要的文件名）
print("✅ 图表已保存为: 折线图_时间序列.png")
plt.show()  # 显示图表

