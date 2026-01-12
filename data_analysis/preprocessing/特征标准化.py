"""
特征标准化与归一化脚本
适用于C题：消除不同特征间量纲的影响，提升模型性能
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler, Normalizer
import matplotlib.pyplot as plt

# ==================== 设置中文字体 ====================
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']  # Mac系统
# plt.rcParams['font.sans-serif'] = ['SimHei']  # Windows系统
plt.rcParams['axes.unicode_minus'] = False

# ==================== 生成示例数据 ====================
np.random.seed(42)

# 创建不同量纲的特征数据（这里替换成你的真实数据）
data = pd.DataFrame({
    '年龄': np.random.randint(20, 60, 100),  # 范围: 20-60
    '收入': np.random.randint(30000, 150000, 100),  # 范围: 30000-150000
    '消费金额': np.random.randint(1000, 50000, 100),  # 范围: 1000-50000
    '登录次数': np.random.randint(1, 500, 100),  # 范围: 1-500
    '评分': np.random.uniform(1, 5, 100)  # 范围: 1-5
})

print("=" * 60)
print("特征标准化与归一化脚本")
print("=" * 60)

print("\n📊 原始数据统计:")
print(data.describe())

print("\n❗ 注意: 不同特征的量纲差异很大！")
print("  年龄: 20-60")
print("  收入: 30000-150000")
print("  这会影响机器学习模型的性能")

# ==================== 方法1: Z-score标准化（最常用）====================
print("\n" + "=" * 60)
print("方法1: Z-score标准化（StandardScaler）")
print("=" * 60)

# 创建标准化器
scaler_standard = StandardScaler()

# 标准化数据（均值为0，标准差为1）
data_standard = pd.DataFrame(
    scaler_standard.fit_transform(data),  # 进行标准化
    columns=data.columns  # 保留列名
)

print("✅ Z-score标准化完成")
print("公式: z = (x - μ) / σ")
print("  其中 μ是均值，σ是标准差")
print("\n标准化后统计:")
print(data_standard.describe())

print("\n各特征的均值和标准差:")
for col in data.columns:
    print(f"  {col}: 均值={data_standard[col].mean():.6f}, 标准差={data_standard[col].std():.6f}")

# ==================== 方法2: Min-Max归一化 ====================
print("\n" + "=" * 60)
print("方法2: Min-Max归一化（MinMaxScaler）")
print("=" * 60)

# 创建归一化器
scaler_minmax = MinMaxScaler(
    feature_range=(0, 1)  # 归一化范围（这里设置为0-1，也可以改为(-1, 1)等）
)

# 归一化数据（缩放到0-1之间）
data_minmax = pd.DataFrame(
    scaler_minmax.fit_transform(data),
    columns=data.columns
)

print("✅ Min-Max归一化完成")
print("公式: x' = (x - min) / (max - min)")
print("\n归一化后统计:")
print(data_minmax.describe())

print("\n各特征的范围:")
for col in data.columns:
    print(f"  {col}: 最小值={data_minmax[col].min():.6f}, 最大值={data_minmax[col].max():.6f}")

# ==================== 方法3: Robust标准化（抗异常值）====================
print("\n" + "=" * 60)
print("方法3: Robust标准化（RobustScaler）")
print("=" * 60)

# 创建鲁棒标准化器
scaler_robust = RobustScaler()

# 标准化数据（使用中位数和IQR，对异常值不敏感）
data_robust = pd.DataFrame(
    scaler_robust.fit_transform(data),
    columns=data.columns
)

print("✅ Robust标准化完成")
print("公式: x' = (x - median) / IQR")
print("  其中 IQR = Q3 - Q1（四分位距）")
print("说明: 此方法对异常值更加稳健")
print("\n标准化后统计:")
print(data_robust.describe())

# ==================== 方法4: L2归一化（行归一化）====================
print("\n" + "=" * 60)
print("方法4: L2归一化（Normalizer）")
print("=" * 60)

# 创建L2归一化器
normalizer = Normalizer(norm='l2')  # norm: 'l1', 'l2', 'max'

# 归一化数据（每个样本的向量长度归一化为1）
data_l2 = pd.DataFrame(
    normalizer.fit_transform(data),
    columns=data.columns
)

print("✅ L2归一化完成")
print("公式: x' = x / ||x||₂")
print("说明: 将每个样本的特征向量归一化为单位长度")
print("\n归一化后统计:")
print(data_l2.describe())

# 验证：每行的L2范数应该为1
row_norms = np.sqrt((data_l2 ** 2).sum(axis=1))
print(f"\n验证: 前5个样本的L2范数={row_norms[:5].values}")

# ==================== 可视化对比 ====================
print("\n" + "=" * 60)
print("📊 可视化对比")
print("=" * 60)

# 选择一个特征进行对比（这里选择'收入'）
feature_to_plot = '收入'  # 可以改成其他特征

fig, axes = plt.subplots(2, 3, figsize=(15, 10), dpi=300)

# 原始数据
axes[0, 0].hist(data[feature_to_plot], bins=20, color='#2E86AB', alpha=0.7, edgecolor='black')
axes[0, 0].set_title(f'原始数据: {feature_to_plot}', fontweight='bold')
axes[0, 0].set_xlabel('数值')
axes[0, 0].set_ylabel('频数')
axes[0, 0].grid(True, alpha=0.3)

# Z-score标准化
axes[0, 1].hist(data_standard[feature_to_plot], bins=20, color='#F18F01', alpha=0.7, edgecolor='black')
axes[0, 1].set_title('Z-score标准化', fontweight='bold')
axes[0, 1].set_xlabel('数值')
axes[0, 1].set_ylabel('频数')
axes[0, 1].grid(True, alpha=0.3)

# Min-Max归一化
axes[0, 2].hist(data_minmax[feature_to_plot], bins=20, color='#6A994E', alpha=0.7, edgecolor='black')
axes[0, 2].set_title('Min-Max归一化', fontweight='bold')
axes[0, 2].set_xlabel('数值')
axes[0, 2].set_ylabel('频数')
axes[0, 2].grid(True, alpha=0.3)

# Robust标准化
axes[1, 0].hist(data_robust[feature_to_plot], bins=20, color='#A23B72', alpha=0.7, edgecolor='black')
axes[1, 0].set_title('Robust标准化', fontweight='bold')
axes[1, 0].set_xlabel('数值')
axes[1, 0].set_ylabel('频数')
axes[1, 0].grid(True, alpha=0.3)

# L2归一化
axes[1, 1].hist(data_l2[feature_to_plot], bins=20, color='#BC4B51', alpha=0.7, edgecolor='black')
axes[1, 1].set_title('L2归一化', fontweight='bold')
axes[1, 1].set_xlabel('数值')
axes[1, 1].set_ylabel('频数')
axes[1, 1].grid(True, alpha=0.3)

# 箱线图对比
bp = axes[1, 2].boxplot([
    data[feature_to_plot],
    data_standard[feature_to_plot],
    data_minmax[feature_to_plot]
], labels=['原始', 'Z-score', 'Min-Max'], patch_artist=True)

for patch, color in zip(bp['boxes'], ['#2E86AB', '#F18F01', '#6A994E']):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)

axes[1, 2].set_title('箱线图对比', fontweight='bold')
axes[1, 2].set_ylabel('数值')
axes[1, 2].grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig('特征标准化对比.png', dpi=300, bbox_inches='tight')
print("✅ 可视化图表已保存为: 特征标准化对比.png")
plt.show()

# ==================== 反向转换（重要！）====================
print("\n" + "=" * 60)
print("⚠️ 反向转换")
print("=" * 60)

# 标准化后的数据可以转换回原始尺度
data_inverse = pd.DataFrame(
    scaler_standard.inverse_transform(data_standard),  # 反向转换
    columns=data.columns
)

print("✅ 已将Z-score标准化的数据转换回原始尺度")
print(f"验证: 原始数据第1行['收入']={data.loc[0, '收入']:.2f}")
print(f"      反向转换后['收入']={data_inverse.loc[0, '收入']:.2f}")

# ==================== 保存处理后的数据和模型 ====================
print("\n" + "=" * 60)
print("💾 保存数据和模型")
print("=" * 60)

# 保存标准化后的数据（选择一种方法）
output_data = data_standard  # 可改为 data_minmax, data_robust, data_l2

output_data.to_csv('处理后的数据_已标准化.csv', index=False, encoding='utf-8-sig')
print("✅ 标准化数据已保存为: 处理后的数据_已标准化.csv")

# 保存标准化器模型（重要！用于测试集）
import joblib
joblib.dump(scaler_standard, '标准化器模型.pkl')  # 保存模型
print("✅ 标准化器已保存为: 标准化器模型.pkl")

print("\n使用保存的标准化器处理新数据:")
print("  scaler = joblib.load('标准化器模型.pkl')")
print("  new_data_scaled = scaler.transform(new_data)")

# ==================== 使用建议 ====================
print("\n" + "=" * 60)
print("💡 方法选择建议")
print("=" * 60)

print("\n何时使用各种方法:")
print("  1. Z-score标准化:")
print("     - 数据近似正态分布")
print("     - 使用SVM、神经网络、KNN等算法")
print("     - ✅ 最常用，推荐首选")
print("\n  2. Min-Max归一化:")
print("     - 需要将数据缩放到特定范围(如0-1)")
print("     - 使用神经网络(sigmoid/tanh激活函数)")
print("     - 数据分布均匀，无极端异常值")
print("\n  3. Robust标准化:")
print("     - 数据中有异常值")
print("     - 数据分布偏斜")
print("     - ✅ 数据质量不佳时推荐")
print("\n  4. L2归一化:")
print("     - 文本数据(TF-IDF)")
print("     - 计算余弦相似度")
print("     - 样本间比较而非特征间比较")

print("\n" + "=" * 60)
print("⚠️ 重要提醒")
print("=" * 60)
print("  1. 先在训练集上fit，再transform训练集和测试集")
print("  2. 不要对测试集单独fit！")
print("  3. 保存标准化器模型，用于预测新数据")
print("  4. 某些特征(如ID、类别)不需要标准化")

print("\n" + "=" * 60)
print("✅ 特征标准化完成！")
print("=" * 60)

