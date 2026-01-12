"""
平行坐标图 - 高维数据可视化
适用于C题：展示客户分群、多目标优化的帕累托解集
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas.plotting import parallel_coordinates
from sklearn.preprocessing import StandardScaler

# ==================== 设置中文字体 ====================
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']  # Mac系统
# plt.rcParams['font.sans-serif'] = ['SimHei']  # Windows系统
plt.rcParams['axes.unicode_minus'] = False

# ==================== 生成示例数据 ====================
np.random.seed(42)
n_samples = 100  # 样本数量

# 创建模拟数据（这里替换成你的真实数据）
data = pd.DataFrame({
    '年龄': np.random.randint(20, 70, n_samples),  # 第1个特征（这里填入你的特征）
    '收入': np.random.randint(30000, 150000, n_samples),  # 第2个特征
    '消费': np.random.randint(1000, 50000, n_samples),  # 第3个特征
    '忠诚度': np.random.rand(n_samples) * 10,  # 第4个特征
    '满意度': np.random.rand(n_samples) * 100  # 第5个特征
})

# 添加分类标签（这里填入你的分类）
# 根据消费水平简单分为3类
data['客户类型'] = pd.cut(data['消费'],
                         bins=3,
                         labels=['低消费', '中消费', '高消费'])

print("📊 数据预览:")
print(data.head())
print(f"\n数据形状: {data.shape}")

# ==================== 数据标准化（重要！消除量纲影响）====================
# 选择需要标准化的数值列
numeric_cols = ['年龄', '收入', '消费', '忠诚度', '满意度']

# 创建标准化器
scaler = StandardScaler()

# 标准化数据（使每个特征的均值为0，标准差为1）
data_normalized = data.copy()
data_normalized[numeric_cols] = scaler.fit_transform(data[numeric_cols])

print("\n📊 标准化后的数据预览:")
print(data_normalized.head())

# ==================== 创建图表 ====================
fig, ax = plt.subplots(figsize=(14, 8), dpi=300)

# ==================== 绘制平行坐标图 ====================
parallel_coordinates(
    data_normalized,  # 标准化后的数据
    '客户类型',  # 分类列名（这里填入你的分类列）
    color=['#2E86AB', '#F18F01', '#6A994E'],  # 每个类别的颜色（根据类别数量调整）
    alpha=0.6,  # 线条透明度（0-1）
    linewidth=2,  # 线条粗细
    ax=ax
)

# ==================== 设置坐标轴和标题 ====================
ax.set_xlabel('特征', fontsize=12, fontweight='bold')  # x轴标签
ax.set_ylabel('标准化数值', fontsize=12, fontweight='bold')  # y轴标签
ax.set_title('客户分群多维特征可视化', fontsize=14, fontweight='bold', pad=20)  # 标题（这里填入你的标题）

# ==================== 设置图例 ====================
ax.legend(
    title='客户类型',  # 图例标题（这里填入你的分类名称）
    loc='upper right',  # 图例位置
    frameon=True,
    shadow=True,
    fontsize=10,
    title_fontsize=11
)

# ==================== 设置网格 ====================
ax.grid(True, alpha=0.3, linestyle='--', linewidth=0.5)

# 旋转x轴标签以便阅读
plt.xticks(rotation=45, ha='right')

# ==================== 添加说明文本 ====================
explanation = '说明: 数据已标准化（均值0，标准差1），便于不同量纲的特征对比'
fig.text(0.5, 0.02, explanation,
         ha='center', fontsize=9, style='italic',
         bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

# ==================== 方式2: 帕累托前沿可视化（多目标优化用）====================
# 如果你的数据是多目标优化的解集，使用以下代码

"""
# 生成帕累托解集示例数据
n_solutions = 50
solutions = pd.DataFrame({
    '成本': np.random.uniform(50, 150, n_solutions),  # 目标1（这里填入你的目标）
    '时间': np.random.uniform(6, 30, n_solutions),   # 目标2
    '质量': np.random.uniform(70, 100, n_solutions), # 目标3
    '风险': np.random.uniform(10, 60, n_solutions),  # 目标4
    '效率': np.random.uniform(20, 100, n_solutions)  # 目标5
})

# 标准化
objective_cols = ['成本', '时间', '质量', '风险', '效率']
solutions_normalized = solutions.copy()
solutions_normalized[objective_cols] = scaler.fit_transform(solutions[objective_cols])

# 创建新图表
fig2, ax2 = plt.subplots(figsize=(14, 8), dpi=300)

# 绘制所有解（灰色）
for i in range(len(solutions_normalized)):
    ax2.plot(range(len(objective_cols)),
            solutions_normalized.iloc[i][objective_cols],
            color='gray', alpha=0.3, linewidth=1)

# 高亮几个代表性解（彩色粗线）
highlight_indices = [5, 15, 30, 45]  # 要高亮的解的索引（这里填入你想高亮的解）
colors_highlight = ['#F18F01', '#C73E1D', '#6A994E', '#2E86AB']

for idx, sol_idx in enumerate(highlight_indices):
    ax2.plot(range(len(objective_cols)),
            solutions_normalized.iloc[sol_idx][objective_cols],
            color=colors_highlight[idx],
            alpha=0.9,
            linewidth=3,
            marker='o',
            markersize=8,
            label=f'方案{sol_idx}')

ax2.set_xticks(range(len(objective_cols)))
ax2.set_xticklabels(objective_cols, rotation=45, ha='right')
ax2.set_xlabel('优化目标', fontsize=12, fontweight='bold')
ax2.set_ylabel('标准化数值', fontsize=12, fontweight='bold')
ax2.set_title('多目标优化帕累托前沿', fontsize=14, fontweight='bold', pad=20)
ax2.legend(frameon=True, shadow=True, loc='best')
ax2.grid(True, alpha=0.3, linestyle='--')

plt.tight_layout()
plt.savefig('平行坐标图_帕累托前沿.png', dpi=300, bbox_inches='tight')
print("✅ 帕累托前沿图已保存为: 平行坐标图_帕累托前沿.png")
"""

# ==================== 统计分析（可选）====================
# 打印每个类别的统计信息
print("\n📊 各类别统计信息:")
for category in data['客户类型'].unique():
    print(f"\n{category}:")
    category_data = data[data['客户类型'] == category][numeric_cols]
    print(category_data.describe().loc[['mean', 'std']])

# ==================== 保存和显示图表 ====================
plt.tight_layout()
plt.savefig('平行坐标图_高维数据.png', dpi=300, bbox_inches='tight')
print("\n✅ 图表已保存为: 平行坐标图_高维数据.png")
plt.show()

