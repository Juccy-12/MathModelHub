"""
散点图 - 相关性分析
适用于C题：探索两个变量之间的关系，计算相关系数和拟合线
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# ==================== 设置中文字体 ====================
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']  # Mac系统
# plt.rcParams['font.sans-serif'] = ['SimHei']  # Windows系统
plt.rcParams['axes.unicode_minus'] = False

# ==================== 生成示例数据 ====================
np.random.seed(42)  # 固定随机种子，保证结果可重现

# 生成数据（这里替换成你的真实数据）
x = np.linspace(0, 10, 50)  # x变量数据（这里填入你的x数据）
y = 2.5 * x + 3 + np.random.normal(0, 2, 50)  # y变量数据（这里填入你的y数据）

# 如果要展示不同类别的散点（可选）
# 生成类别标签
categories = np.random.choice(['类别A', '类别B', '类别C'], 50)

# ==================== 计算线性回归和相关系数（O奖必备！）====================
# 计算线性回归参数
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
line = slope * x + intercept  # 拟合直线

# 计算相关系数
r_squared = r_value ** 2  # R²决定系数

print(f"📊 回归方程: y = {slope:.3f}x + {intercept:.3f}")
print(f"📊 相关系数 R² = {r_squared:.4f}")
print(f"📊 p值 = {p_value:.4e}")

# ==================== 创建图表 ====================
fig, ax = plt.subplots(figsize=(10, 8), dpi=300)

# ==================== 方式1: 简单散点图 ====================
# 绘制散点
scatter = ax.scatter(x, y,
                    c='#2E86AB',  # 散点颜色
                    s=80,  # 散点大小
                    alpha=0.6,  # 透明度
                    edgecolors='black',  # 边框颜色
                    linewidth=0.5,  # 边框宽度
                    label='数据点')  # 图例标签

# ==================== 方式2: 按类别着色的散点图（可选）====================
# 取消注释以下代码来使用分类散点图
"""
colors = {'类别A': '#2E86AB', '类别B': '#F18F01', '类别C': '#6A994E'}
for category in ['类别A', '类别B', '类别C']:
    mask = categories == category
    ax.scatter(x[mask], y[mask],
              c=colors[category],
              s=80,
              alpha=0.7,
              edgecolors='black',
              linewidth=0.5,
              label=category)
"""

# ==================== 绘制拟合线 ====================
ax.plot(x, line,
        'r-',  # 红色实线
        linewidth=2.5,  # 线条宽度
        label='线性拟合',  # 图例标签
        alpha=0.8)

# ==================== 添加回归方程和R²（O奖必备！）====================
# 在图上显示回归方程和R²
equation_text = f'y = {slope:.3f}x + {intercept:.3f}\n$R^2$ = {r_squared:.4f}\np < {p_value:.4f}'
ax.text(0.05, 0.95,  # 文本框位置（0-1的相对坐标）
        equation_text,  # 显示的文本
        transform=ax.transAxes,  # 使用相对坐标
        fontsize=11,
        verticalalignment='top',  # 垂直对齐方式
        bbox=dict(boxstyle='round',  # 文本框样式
                 facecolor='wheat',  # 背景颜色
                 alpha=0.8,  # 透明度
                 edgecolor='black',  # 边框颜色
                 linewidth=1.5))

# ==================== 添加密度等高线（可选，高级）====================
# 取消注释以下代码来添加密度等高线
"""
from scipy.stats import gaussian_kde
# 计算密度
xy = np.vstack([x, y])
z = gaussian_kde(xy)(xy)
# 绘制等高线
contour = ax.tricontour(x, y, z, levels=5, linewidths=0.5, colors='gray', alpha=0.4)
"""

# ==================== 标注异常点（可选）====================
# 找出离拟合线较远的点
residuals = np.abs(y - line)
outlier_threshold = 2 * np.std(residuals)  # 阈值：2倍标准差
outliers = residuals > outlier_threshold

# 标注异常点
if np.any(outliers):
    ax.scatter(x[outliers], y[outliers],
              c='red',
              s=150,
              marker='x',
              linewidth=2,
              label='异常点')

# ==================== 设置坐标轴和标题 ====================
ax.set_xlabel('特征X', fontsize=12, fontweight='bold')  # x轴标签（这里填入你的x变量名）
ax.set_ylabel('特征Y', fontsize=12, fontweight='bold')  # y轴标签（这里填入你的y变量名）
ax.set_title('变量相关性分析与线性回归', fontsize=14, fontweight='bold', pad=20)  # 标题

# ==================== 设置图例 ====================
ax.legend(loc='lower right',  # 图例位置
          frameon=True,
          shadow=True,
          fontsize=10)

# ==================== 设置网格 ====================
ax.grid(True, alpha=0.3, linestyle='--', linewidth=0.5)

# ==================== 保存和显示图表 ====================
plt.tight_layout()
plt.savefig('散点图_相关性分析.png', dpi=300, bbox_inches='tight')
print("✅ 图表已保存为: 散点图_相关性分析.png")
plt.show()

