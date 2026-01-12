"""
缺失值处理脚本
适用于C题：处理数据集中的缺失值，提供多种填充策略
"""

import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer, KNNImputer

# ==================== 设置显示选项 ====================
pd.set_option('display.max_columns', None)  # 显示所有列
pd.set_option('display.width', 1000)  # 设置显示宽度

# ==================== 生成示例数据（含缺失值）====================
np.random.seed(42)

# 创建示例数据集（这里替换成你的真实数据）
data = pd.DataFrame({
    '用户ID': range(1, 101),  # 用户ID（这里填入你的数据）
    '年龄': np.random.randint(20, 60, 100),  # 年龄
    '收入': np.random.randint(30000, 100000, 100),  # 收入
    '消费金额': np.random.randint(1000, 10000, 100),  # 消费金额
    '登录次数': np.random.randint(1, 100, 100),  # 登录次数
    '类别': np.random.choice(['A', 'B', 'C'], 100)  # 类别变量
})

# 人为制造一些缺失值（模拟真实情况）
missing_indices_age = np.random.choice(100, 15, replace=False)  # 15个缺失值
missing_indices_income = np.random.choice(100, 20, replace=False)  # 20个缺失值
missing_indices_amount = np.random.choice(100, 10, replace=False)  # 10个缺失值

data.loc[missing_indices_age, '年龄'] = np.nan
data.loc[missing_indices_income, '收入'] = np.nan
data.loc[missing_indices_amount, '消费金额'] = np.nan

print("=" * 60)
print("缺失值处理脚本")
print("=" * 60)

# ==================== 1. 查看缺失值情况 ====================
print("\n📊 原始数据预览:")
print(data.head(10))

print("\n📊 缺失值统计:")
missing_stats = pd.DataFrame({
    '缺失数量': data.isnull().sum(),  # 每列缺失值数量
    '缺失比例': (data.isnull().sum() / len(data) * 100).round(2)  # 缺失比例（%）
})
print(missing_stats[missing_stats['缺失数量'] > 0])  # 只显示有缺失的列

# ==================== 2. 删除缺失值（适合缺失比例很小的情况）====================
print("\n" + "=" * 60)
print("方法1: 删除缺失值")
print("=" * 60)

# 删除包含任何缺失值的行
data_drop_rows = data.dropna()  # 删除任何列有缺失的行
print(f"删除行后剩余样本数: {len(data_drop_rows)} / {len(data)} ({len(data_drop_rows)/len(data)*100:.1f}%)")

# 删除缺失值过多的列（可选）
threshold = 0.5  # 缺失比例阈值（这里设置为50%，可以调整）
data_drop_cols = data.dropna(thresh=int(len(data) * threshold), axis=1)
print(f"删除列后剩余特征数: {data_drop_cols.shape[1]} / {data.shape[1]}")

# ==================== 3. 均值/中位数/众数填充 ====================
print("\n" + "=" * 60)
print("方法2: 统计量填充")
print("=" * 60)

# 方法2.1: 均值填充（适合数值型特征，数据分布较均匀）
data_mean = data.copy()
imputer_mean = SimpleImputer(strategy='mean')  # 策略：'mean'均值, 'median'中位数, 'most_frequent'众数
numeric_cols = ['年龄', '收入', '消费金额', '登录次数']  # 数值型列（这里填入你的数值列名）
data_mean[numeric_cols] = imputer_mean.fit_transform(data_mean[numeric_cols])

print("✅ 均值填充完成")
print("填充值:")
for i, col in enumerate(numeric_cols):
    if col in data.columns:
        fill_value = imputer_mean.statistics_[i]
        print(f"  {col}: {fill_value:.2f}")

# 方法2.2: 中位数填充（适合有异常值的情况）
data_median = data.copy()
imputer_median = SimpleImputer(strategy='median')
data_median[numeric_cols] = imputer_median.fit_transform(data_median[numeric_cols])

print("\n✅ 中位数填充完成")
print("填充值:")
for i, col in enumerate(numeric_cols):
    if col in data.columns:
        fill_value = imputer_median.statistics_[i]
        print(f"  {col}: {fill_value:.2f}")

# 方法2.3: 众数填充（适合类别型特征）
data_mode = data.copy()
imputer_mode = SimpleImputer(strategy='most_frequent')
categorical_cols = ['类别']  # 类别型列（这里填入你的类别列名）
if categorical_cols:
    data_mode[categorical_cols] = imputer_mode.fit_transform(data_mode[categorical_cols])
    print("\n✅ 众数填充完成（类别变量）")

# ==================== 4. KNN填充（考虑样本间的相似性）====================
print("\n" + "=" * 60)
print("方法3: KNN填充（推荐！）")
print("=" * 60)

# KNN填充：根据最近邻的K个样本来填充
data_knn = data.copy()
imputer_knn = KNNImputer(
    n_neighbors=5,  # K值（邻居数量，这里设置为5，可以调整为3-10）
    weights='uniform'  # 权重方式：'uniform'均匀权重, 'distance'距离加权
)

# 只对数值列进行KNN填充
data_knn[numeric_cols] = imputer_knn.fit_transform(data_knn[numeric_cols])

print(f"✅ KNN填充完成（K={5}）")
print("说明: KNN会根据相似样本的值来填充，比简单统计量更准确")

# ==================== 5. 前向/后向填充（适合时间序列）====================
print("\n" + "=" * 60)
print("方法4: 前向/后向填充（时间序列专用）")
print("=" * 60)

# 前向填充：用前一个有效值填充
data_ffill = data.copy()
data_ffill = data_ffill.fillna(method='ffill')  # method: 'ffill'前向填充, 'bfill'后向填充

print("✅ 前向填充完成")
print("说明: 用前一个时间点的值填充当前缺失值")

# 后向填充：用后一个有效值填充
data_bfill = data.copy()
data_bfill = data_bfill.fillna(method='bfill')

print("✅ 后向填充完成")

# ==================== 6. 固定值填充 ====================
print("\n" + "=" * 60)
print("方法5: 固定值填充")
print("=" * 60)

# 用指定的固定值填充
data_fixed = data.copy()
fill_values = {
    '年龄': 30,  # 用30填充年龄的缺失值（这里填入你想用的值）
    '收入': 50000,  # 用50000填充收入的缺失值
    '消费金额': 5000  # 用5000填充消费金额的缺失值
}

data_fixed = data_fixed.fillna(value=fill_values)

print("✅ 固定值填充完成")
print("填充值:")
for col, val in fill_values.items():
    print(f"  {col}: {val}")

# ==================== 7. 验证填充效果 ====================
print("\n" + "=" * 60)
print("📊 填充效果对比")
print("=" * 60)

methods = {
    '原始数据': data,
    '均值填充': data_mean,
    '中位数填充': data_median,
    'KNN填充': data_knn,
    '前向填充': data_ffill
}

print("\n各方法剩余缺失值数量:")
for method_name, method_data in methods.items():
    missing_count = method_data.isnull().sum().sum()
    print(f"  {method_name}: {missing_count}个缺失值")

# ==================== 8. 保存处理后的数据 ====================
print("\n" + "=" * 60)
print("💾 保存数据")
print("=" * 60)

# 选择一种方法保存（这里选择KNN填充，你可以改成其他方法）
output_data = data_knn  # 选择要保存的数据（data_mean, data_median, data_knn等）

# 保存为CSV文件
output_data.to_csv('处理后的数据_缺失值已填充.csv', index=False, encoding='utf-8-sig')
print("✅ 数据已保存为: 处理后的数据_缺失值已填充.csv")

# ==================== 9. 可视化对比（可选）====================
print("\n" + "=" * 60)
print("📊 统计对比")
print("=" * 60)

# 对比填充前后的统计量
print("\n年龄统计对比:")
print(f"  原始数据均值: {data['年龄'].mean():.2f}")
print(f"  KNN填充后均值: {data_knn['年龄'].mean():.2f}")
print(f"  原始数据标准差: {data['年龄'].std():.2f}")
print(f"  KNN填充后标准差: {data_knn['年龄'].std():.2f}")

print("\n收入统计对比:")
print(f"  原始数据均值: {data['收入'].mean():.2f}")
print(f"  KNN填充后均值: {data_knn['收入'].mean():.2f}")

print("\n" + "=" * 60)
print("✅ 缺失值处理完成！")
print("=" * 60)

# ==================== 使用建议 ====================
print("\n💡 方法选择建议:")
print("  1. 缺失很少(<5%): 直接删除")
print("  2. 数值型特征，分布均匀: 均值填充")
print("  3. 数值型特征，有异常值: 中位数填充")
print("  4. 类别型特征: 众数填充")
print("  5. 样本间有相关性: KNN填充（推荐！）")
print("  6. 时间序列数据: 前向/后向填充")
print("  7. 有业务含义的默认值: 固定值填充")

