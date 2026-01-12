"""
异常值检测与处理脚本
适用于C题：检测并处理数据中的异常值（离群点）
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.ensemble import IsolationForest
from sklearn.covariance import EllipticEnvelope

# ==================== 设置中文字体 ====================
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']  # Mac系统
# plt.rcParams['font.sans-serif'] = ['SimHei']  # Windows系统
plt.rcParams['axes.unicode_minus'] = False

# ==================== 生成示例数据 ====================
np.random.seed(42)

# 创建正常数据（这里替换成你的真实数据）
n_samples = 200
data = pd.DataFrame({
    '特征1': np.random.normal(50, 10, n_samples),  # 均值50，标准差10
    '特征2': np.random.normal(100, 20, n_samples),  # 均值100，标准差20
    '特征3': np.random.normal(30, 5, n_samples)  # 均值30，标准差5
})

# 添加一些异常值（模拟真实情况）
n_outliers = 10  # 异常值数量
outlier_indices = np.random.choice(n_samples, n_outliers, replace=False)
data.loc[outlier_indices, '特征1'] += np.random.uniform(50, 100, n_outliers)  # 在某些样本中添加异常值
data.loc[outlier_indices[:5], '特征2'] -= np.random.uniform(80, 120, 5)

print("=" * 60)
print("异常值检测与处理脚本")
print("=" * 60)

print("\n📊 原始数据统计:")
print(data.describe())

# ==================== 方法1: 3σ原则（标准差法）====================
print("\n" + "=" * 60)
print("方法1: 3σ原则（标准差法）")
print("=" * 60)

def detect_outliers_zscore(data, columns, threshold=3):
    """
    使用Z-score方法检测异常值
    
    参数:
        data: DataFrame
        columns: 要检测的列名列表
        threshold: 阈值（通常设置为3，表示3倍标准差）
    """
    outliers = pd.DataFrame()
    
    for col in columns:
        # 计算Z-score
        z_scores = np.abs(stats.zscore(data[col]))  # 计算标准分数
        
        # 找出异常值
        outlier_mask = z_scores > threshold  # 超过阈值的视为异常
        outliers[col] = outlier_mask
        
        n_outliers = outlier_mask.sum()
        print(f"\n{col}:")
        print(f"  检测到{n_outliers}个异常值 ({n_outliers/len(data)*100:.1f}%)")
        print(f"  均值: {data[col].mean():.2f}, 标准差: {data[col].std():.2f}")
        print(f"  异常值范围: > {data[col].mean() + threshold*data[col].std():.2f} "
              f"或 < {data[col].mean() - threshold*data[col].std():.2f}")
    
    return outliers

# 检测异常值
numeric_cols = ['特征1', '特征2', '特征3']  # 数值型列（这里填入你的列名）
outliers_zscore = detect_outliers_zscore(data, numeric_cols, threshold=3)  # 阈值可调整为2-4

# 找出至少在一个特征上是异常值的样本
any_outlier_zscore = outliers_zscore.any(axis=1)
print(f"\n总计: {any_outlier_zscore.sum()}个样本被标记为异常")

# ==================== 方法2: IQR法（四分位距法）====================
print("\n" + "=" * 60)
print("方法2: IQR法（四分位距法）")
print("=" * 60)

def detect_outliers_iqr(data, columns, k=1.5):
    """
    使用IQR方法检测异常值
    
    参数:
        data: DataFrame
        columns: 要检测的列名列表
        k: IQR倍数（通常设置为1.5，可调整为1-3）
    """
    outliers = pd.DataFrame()
    
    for col in columns:
        Q1 = data[col].quantile(0.25)  # 第一四分位数（25%）
        Q3 = data[col].quantile(0.75)  # 第三四分位数（75%）
        IQR = Q3 - Q1  # 四分位距
        
        # 计算异常值边界
        lower_bound = Q1 - k * IQR  # 下界
        upper_bound = Q3 + k * IQR  # 上界
        
        # 找出异常值
        outlier_mask = (data[col] < lower_bound) | (data[col] > upper_bound)
        outliers[col] = outlier_mask
        
        n_outliers = outlier_mask.sum()
        print(f"\n{col}:")
        print(f"  Q1={Q1:.2f}, Q3={Q3:.2f}, IQR={IQR:.2f}")
        print(f"  异常值范围: < {lower_bound:.2f} 或 > {upper_bound:.2f}")
        print(f"  检测到{n_outliers}个异常值 ({n_outliers/len(data)*100:.1f}%)")
    
    return outliers

# 检测异常值
outliers_iqr = detect_outliers_iqr(data, numeric_cols, k=1.5)  # k可调整为1-3

# 找出至少在一个特征上是异常值的样本
any_outlier_iqr = outliers_iqr.any(axis=1)
print(f"\n总计: {any_outlier_iqr.sum()}个样本被标记为异常")

# ==================== 方法3: Isolation Forest（孤立森林）====================
print("\n" + "=" * 60)
print("方法3: Isolation Forest（推荐！）")
print("=" * 60)

# 训练孤立森林模型
iso_forest = IsolationForest(
    contamination=0.1,  # 预期异常值比例（这里设置为10%，根据实际情况调整0.01-0.2）
    random_state=42,  # 随机种子
    n_estimators=100  # 树的数量（默认100，可调整）
)

# 预测异常值（-1表示异常，1表示正常）
outlier_predictions = iso_forest.fit_predict(data[numeric_cols])
outliers_iforest = outlier_predictions == -1  # True表示异常

print(f"检测到{outliers_iforest.sum()}个异常值 ({outliers_iforest.sum()/len(data)*100:.1f}%)")
print("说明: Isolation Forest通过构建随机树来隔离异常点")

# ==================== 处理异常值的方法 ====================
print("\n" + "=" * 60)
print("📊 异常值处理方法")
print("=" * 60)

# 选择一种检测方法的结果（这里选择IQR法）
outlier_mask = any_outlier_iqr  # 可改为 any_outlier_zscore 或 outliers_iforest

# 处理方法1: 删除异常值
print("\n方法A: 删除异常值")
data_removed = data[~outlier_mask].copy()  # ~表示取反，保留非异常值
print(f"  删除前: {len(data)}个样本")
print(f"  删除后: {len(data_removed)}个样本")
print(f"  删除了: {outlier_mask.sum()}个样本 ({outlier_mask.sum()/len(data)*100:.1f}%)")

# 处理方法2: 用边界值替换（Winsorize）
print("\n方法B: 边界值替换（Winsorize）")
data_winsorized = data.copy()

for col in numeric_cols:
    # 计算边界值（使用IQR方法）
    Q1 = data[col].quantile(0.25)
    Q3 = data[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    # 替换异常值
    data_winsorized.loc[data_winsorized[col] < lower_bound, col] = lower_bound
    data_winsorized.loc[data_winsorized[col] > upper_bound, col] = upper_bound
    
    replaced = ((data[col] < lower_bound) | (data[col] > upper_bound)).sum()
    print(f"  {col}: 替换了{replaced}个异常值")

# 处理方法3: 用中位数/均值替换
print("\n方法C: 中位数替换")
data_median = data.copy()

for col in numeric_cols:
    median_val = data[col].median()  # 中位数（也可以用mean()均值）
    outlier_col = outliers_iqr[col]  # 该列的异常值标记
    data_median.loc[outlier_col, col] = median_val  # 替换异常值
    
    replaced = outlier_col.sum()
    if replaced > 0:
        print(f"  {col}: 用中位数{median_val:.2f}替换了{replaced}个异常值")

# 处理方法4: 保留异常值但标记
print("\n方法D: 标记异常值（保留数据）")
data_flagged = data.copy()
data_flagged['是否异常'] = outlier_mask.astype(int)  # 添加异常值标记列
print(f"  添加了'是否异常'列，1表示异常，0表示正常")

# ==================== 可视化对比 ====================
print("\n" + "=" * 60)
print("📊 可视化异常值")
print("=" * 60)

fig, axes = plt.subplots(1, 3, figsize=(15, 5), dpi=300)

for i, col in enumerate(numeric_cols):
    ax = axes[i]
    
    # 绘制箱线图
    bp = ax.boxplot([data[col]], labels=[col], patch_artist=True)
    bp['boxes'][0].set_facecolor('#2E86AB')
    bp['boxes'][0].set_alpha(0.7)
    
    # 标注异常值
    outlier_data = data.loc[outliers_iqr[col], col]
    if len(outlier_data) > 0:
        ax.scatter([1] * len(outlier_data), outlier_data,
                  color='red', s=50, alpha=0.6, label='异常值')
    
    ax.set_title(f'{col}的分布', fontweight='bold')
    ax.set_ylabel('数值')
    ax.grid(True, alpha=0.3)
    if i == 0:
        ax.legend()

plt.tight_layout()
plt.savefig('异常值检测结果.png', dpi=300, bbox_inches='tight')
print("✅ 可视化图表已保存为: 异常值检测结果.png")
plt.show()

# ==================== 保存处理后的数据 ====================
print("\n" + "=" * 60)
print("💾 保存数据")
print("=" * 60)

# 选择一种处理方法保存（这里选择边界值替换）
output_data = data_winsorized  # 可改为 data_removed, data_median, data_flagged

output_data.to_csv('处理后的数据_异常值已处理.csv', index=False, encoding='utf-8-sig')
print("✅ 数据已保存为: 处理后的数据_异常值已处理.csv")

# ==================== 统计对比 ====================
print("\n" + "=" * 60)
print("📊 处理前后对比")
print("=" * 60)

print("\n特征1统计对比:")
print(f"  原始数据: 均值={data['特征1'].mean():.2f}, 标准差={data['特征1'].std():.2f}")
print(f"  处理后: 均值={data_winsorized['特征1'].mean():.2f}, 标准差={data_winsorized['特征1'].std():.2f}")

print("\n" + "=" * 60)
print("✅ 异常值处理完成！")
print("=" * 60)

# ==================== 使用建议 ====================
print("\n💡 方法选择建议:")
print("  检测方法:")
print("    - 单变量分析: 3σ法或IQR法")
print("    - 多变量分析: Isolation Forest（推荐！）")
print("  处理方法:")
print("    - 异常值很少: 删除")
print("    - 数据宝贵: 边界值替换（Winsorize）")
print("    - 需要稳健性: 中位数替换")
print("    - 需要追溯: 仅标记，不删除")

