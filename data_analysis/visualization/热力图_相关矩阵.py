"""
热力图 - 相关系数矩阵
适用于C题：展示多个特征之间的相关性，用于特征选择
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# ==================== 设置中文字体 ====================
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']  # Mac系统
# plt.rcParams['font.sans-serif'] = ['SimHei']  # Windows系统
plt.rcParams['axes.unicode_minus'] = False

# ==================== 生成示例数据 ====================
np.random.seed(42)
n_samples = 100  # 样本数量

# 创建模拟数据（这里替换成你的真实数据）
data = pd.DataFrame({
    '用户活跃度': np.random.randn(n_samples),  # 第1个特征（这里填入你的特征名）
    '消费金额': np.random.randn(n_samples),     # 第2个特征
    '登录次数': np.random.randn(n_samples),     # 第3个特征
    '浏览时长': np.random.randn(n_samples),     # 第4个特征
    '购买频率': np.random.randn(n_samples),     # 第5个特征
    '客户满意度': np.random.randn(n_samples)    # 第6个特征
})

# 创建一些相关性（让数据更真实）
data['消费金额'] = data['用户活跃度'] * 0.7 + np.random.randn(n_samples) * 0.3
data['购买频率'] = data['消费金额'] * 0.6 + np.random.randn(n_samples) * 0.4
data['客户满意度'] = -data['登录次数'] * 0.5 + np.random.randn(n_samples) * 0.5

# ==================== 计算相关系数矩阵 ====================
# 计算皮尔逊相关系数
correlation_matrix = data.corr(method='pearson')  # 相关系数类型：'pearson', 'spearman', 'kendall'

print("📊 相关系数矩阵:")
print(correlation_matrix)

# ==================== 创建图表 ====================
fig, ax = plt.subplots(figsize=(10, 8), dpi=300)

# ==================== 绘制热力图（O奖高频图表！）====================
heatmap = sns.heatmap(
    correlation_matrix,  # 相关系数矩阵数据
    annot=True,  # 是否在格子中显示数值（True/False）
    fmt='.2f',  # 数值格式（'.2f'保留2位小数, '.3f'保留3位小数）
    cmap='RdBu_r',  # 颜色映射（'RdBu_r'红蓝, 'coolwarm'冷暖, 'YlOrRd'黄橙红, 'viridis'渐变）
    center=0,  # 颜色中心值（通常设为0，使正负相关区分明显）
    vmin=-1,  # 颜色条最小值
    vmax=1,  # 颜色条最大值
    square=True,  # 是否使用正方形格子
    linewidths=0.5,  # 格子间的线宽
    linecolor='white',  # 格子间的线颜色
    cbar_kws={
        'label': '皮尔逊相关系数',  # 颜色条标签（这里填入你使用的相关系数类型）
        'shrink': 0.8,  # 颜色条大小
        'orientation': 'vertical'  # 颜色条方向（'vertical'垂直, 'horizontal'水平）
    },
    ax=ax
)

# ==================== 自定义样式 ====================
# 设置刻度标签样式
ax.set_xticklabels(ax.get_xticklabels(),
                   rotation=45,  # 旋转角度（0-90度）
                   ha='right',  # 水平对齐方式
                   fontsize=10)

ax.set_yticklabels(ax.get_yticklabels(),
                   rotation=0,  # y轴标签不旋转
                   fontsize=10)

# ==================== 设置标题 ====================
ax.set_title('特征相关性矩阵分析', fontsize=14, fontweight='bold', pad=20)  # 标题（这里填入你的标题）

# ==================== 添加说明文本（可选）====================
# 在图下方添加说明
explanation_text = (
    '说明: 红色表示正相关，蓝色表示负相关\n'
    '数值越接近1或-1，相关性越强；接近0则相关性弱'
)
fig.text(0.5, -0.05,  # 文本位置
         explanation_text,
         ha='center',  # 水平对齐
         fontsize=9,
         style='italic',  # 斜体
         bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

# ==================== 方式2: 只显示下三角矩阵（可选）====================
# 取消注释以下代码来只显示下三角
"""
fig2, ax2 = plt.subplots(figsize=(10, 8), dpi=300)

# 创建掩码，只显示下三角
mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))

sns.heatmap(
    correlation_matrix,
    mask=mask,  # 使用掩码
    annot=True,
    fmt='.2f',
    cmap='RdBu_r',
    center=0,
    vmin=-1,
    vmax=1,
    square=True,
    linewidths=0.5,
    cbar_kws={'label': '相关系数', 'shrink': 0.8},
    ax=ax2
)

ax2.set_title('相关系数矩阵（下三角）', fontsize=14, fontweight='bold', pad=20)
ax2.set_xticklabels(ax2.get_xticklabels(), rotation=45, ha='right')
plt.tight_layout()
plt.savefig('热力图_相关矩阵_下三角.png', dpi=300, bbox_inches='tight')
"""

# ==================== 找出强相关特征对（可选）====================
# 找出相关系数绝对值大于0.7的特征对
threshold = 0.7  # 阈值（这里可以调整，通常0.6-0.8）
high_corr_pairs = []

for i in range(len(correlation_matrix.columns)):
    for j in range(i+1, len(correlation_matrix.columns)):
        if abs(correlation_matrix.iloc[i, j]) > threshold:
            high_corr_pairs.append({
                '特征1': correlation_matrix.columns[i],
                '特征2': correlation_matrix.columns[j],
                '相关系数': correlation_matrix.iloc[i, j]
            })

if high_corr_pairs:
    print(f"\n📊 强相关特征对（|r| > {threshold}）:")
    for pair in high_corr_pairs:
        print(f"   {pair['特征1']} <-> {pair['特征2']}: {pair['相关系数']:.3f}")
else:
    print(f"\n📊 没有发现强相关特征对（|r| > {threshold}）")

# ==================== 保存和显示图表 ====================
plt.tight_layout()
plt.savefig('热力图_相关矩阵.png', dpi=300, bbox_inches='tight')
print("\n✅ 图表已保存为: 热力图_相关矩阵.png")
plt.show()

