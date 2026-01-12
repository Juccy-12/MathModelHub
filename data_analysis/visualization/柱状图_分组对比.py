"""
柱状图 - 分组对比
适用于C题：对比不同模型/方法在多个指标上的性能
"""

import matplotlib.pyplot as plt
import numpy as np

# ==================== 设置中文字体 ====================
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']  # Mac系统
# plt.rcParams['font.sans-serif'] = ['SimHei']  # Windows系统
plt.rcParams['axes.unicode_minus'] = False

# ==================== 准备数据 ====================
# 类别名称（这里填入你的方法/模型名称）
categories = ['模型A', '模型B', '模型C', '模型D']

# 多个指标的数据（这里填入你的真实数据）
accuracy = [0.85, 0.90, 0.82, 0.88]  # 准确率（替换成你的第1个指标数据）
precision = [0.82, 0.87, 0.80, 0.85]  # 精确率（替换成你的第2个指标数据）
recall = [0.88, 0.92, 0.85, 0.90]  # 召回率（替换成你的第3个指标数据）
f1_score = [0.85, 0.89, 0.82, 0.87]  # F1分数（替换成你的第4个指标数据）

# ==================== 创建图表 ====================
fig, ax = plt.subplots(figsize=(12, 6), dpi=300)

# 设置柱子的位置和宽度
x = np.arange(len(categories))  # 类别的位置
width = 0.2  # 每个柱子的宽度（可以调整，建议0.15-0.25）

# 绘制每组柱子
bar1 = ax.bar(x - 1.5*width, accuracy,  # 第1组柱子（向左偏移）
              width,
              label='准确率',  # 图例标签（这里填入你的指标名称）
              color='#2E86AB',  # 柱子颜色
              alpha=0.85,  # 透明度
              edgecolor='black',  # 边框颜色
              linewidth=0.8)  # 边框宽度

bar2 = ax.bar(x - 0.5*width, precision,  # 第2组柱子
              width,
              label='精确率',
              color='#A23B72',
              alpha=0.85,
              edgecolor='black',
              linewidth=0.8)

bar3 = ax.bar(x + 0.5*width, recall,  # 第3组柱子
              width,
              label='召回率',
              color='#F18F01',
              alpha=0.85,
              edgecolor='black',
              linewidth=0.8)

bar4 = ax.bar(x + 1.5*width, f1_score,  # 第4组柱子（向右偏移）
              width,
              label='F1分数',
              color='#6A994E',
              alpha=0.85,
              edgecolor='black',
              linewidth=0.8)

# ==================== 在柱子顶部添加数值标注（O奖加分项！）====================
def add_value_labels(bars):
    """在柱子顶部添加数值"""
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2.,  # x位置（柱子中心）
                height,  # y位置（柱子顶部）
                f'{height:.2f}',  # 显示的文本（保留2位小数）
                ha='center',  # 水平对齐方式
                va='bottom',  # 垂直对齐方式
                fontsize=8,  # 字体大小
                fontweight='bold')  # 字体粗细

# 为每组柱子添加数值标注
add_value_labels(bar1)
add_value_labels(bar2)
add_value_labels(bar3)
add_value_labels(bar4)

# ==================== 设置坐标轴和标题 ====================
ax.set_xlabel('模型', fontsize=12, fontweight='bold')  # x轴标签
ax.set_ylabel('得分', fontsize=12, fontweight='bold')  # y轴标签（这里填入你的指标单位）
ax.set_title('不同模型在多个指标上的性能对比', fontsize=14, fontweight='bold', pad=20)  # 标题

# 设置x轴刻度
ax.set_xticks(x)
ax.set_xticklabels(categories, rotation=0)  # rotation为标签旋转角度（0, 45, 90等）

# 设置y轴范围（可选）
ax.set_ylim(0, 1.0)  # y轴范围（这里根据你的数据调整）

# ==================== 设置图例 ====================
ax.legend(loc='upper left',  # 图例位置
          frameon=True,
          shadow=True,
          fontsize=10,
          ncol=4)  # 图例列数（这里设置为4列横向排列）

# ==================== 设置网格 ====================
ax.grid(True, axis='y', alpha=0.3, linestyle='--', linewidth=0.5)  # 只显示y轴网格

# ==================== 保存和显示图表 ====================
plt.tight_layout()
plt.savefig('柱状图_分组对比.png', dpi=300, bbox_inches='tight')
print("✅ 图表已保存为: 柱状图_分组对比.png")
plt.show()

