# 数据预处理模块

## 📁 文件列表

| 文件 | 功能 | 适用场景 |
|-----|------|---------|
| `缺失值处理.py` | 检测和填充缺失数据 | 数据清洗、数据质量提升 |
| `异常值处理.py` | 检测和处理离群点 | 提高模型鲁棒性 |
| `特征标准化.py` | 特征缩放和归一化 | 消除量纲影响，提升模型性能 |

## 🚀 快速开始

### 1. 安装依赖
```bash
pip install pandas numpy scikit-learn scipy matplotlib
```

### 2. 运行脚本
```bash
cd data_analysis/preprocessing

# 处理缺失值
python 缺失值处理.py

# 处理异常值
python 异常值处理.py

# 特征标准化
python 特征标准化.py
```

## 📊 各脚本详细说明

### 1. 缺失值处理.py

**功能**: 检测和填充数据中的缺失值

**包含方法**:
1. **删除法** - 直接删除含缺失值的行/列
2. **均值/中位数/众数填充** - 用统计量填充
3. **KNN填充** - 根据相似样本填充（推荐！）
4. **前向/后向填充** - 时间序列专用
5. **固定值填充** - 用指定值填充

**使用建议**:
- 缺失<5%: 直接删除
- 数值型特征: 均值/中位数/KNN填充
- 类别型特征: 众数填充
- 时间序列: 前向/后向填充
- ✅ **推荐**: KNN填充（考虑样本相似性）

---

### 2. 异常值处理.py

**功能**: 检测和处理数据中的离群点

**检测方法**:
1. **3σ原则** - 基于均值和标准差
2. **IQR法** - 基于四分位距
3. **Isolation Forest** - 机器学习方法（推荐！）

**处理方法**:
1. **删除** - 直接删除异常样本
2. **边界值替换** - Winsorize方法
3. **中位数替换** - 用中位数填充
4. **仅标记** - 保留数据，添加标记列

**使用建议**:
- 检测: Isolation Forest（多变量）
- 处理: 数据少用删除，数据多用替换
- ✅ **推荐**: 边界值替换（保留数据结构）

---

### 3. 特征标准化.py

**功能**: 消除不同特征间的量纲差异

**标准化方法**:
1. **Z-score标准化** - 均值0，标准差1（最常用）
2. **Min-Max归一化** - 缩放到0-1区间
3. **Robust标准化** - 抗异常值
4. **L2归一化** - 样本向量归一化

**使用建议**:
- SVM/神经网络: Z-score标准化
- 有异常值: Robust标准化
- 需要0-1范围: Min-Max归一化
- 文本数据: L2归一化
- ✅ **推荐**: Z-score标准化（最常用）

---

## 💡 数据预处理流程

### 标准流程（按顺序执行）

```
1. 缺失值处理 → 2. 异常值处理 → 3. 特征标准化
```

### 详细步骤

#### 第1步: 处理缺失值
```bash
python 缺失值处理.py
```
- 检查缺失比例
- 选择填充方法
- 保存处理后的数据

#### 第2步: 处理异常值
```bash
python 异常值处理.py
```
- 检测离群点
- 选择处理策略
- 保存处理后的数据

#### 第3步: 特征标准化
```bash
python 特征标准化.py
```
- 选择标准化方法
- 保存标准化器模型
- 用于训练机器学习模型

---

## 📝 使用示例

### 完整的数据预处理工作流

```python
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.impute import KNNImputer

# 1. 读取数据
data = pd.read_csv('原始数据.csv')

# 2. 处理缺失值（KNN填充）
imputer = KNNImputer(n_neighbors=5)
data_filled = pd.DataFrame(
    imputer.fit_transform(data),
    columns=data.columns
)

# 3. 处理异常值（边界值替换）
for col in numeric_cols:
    Q1 = data_filled[col].quantile(0.25)
    Q3 = data_filled[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    data_filled[col] = data_filled[col].clip(lower, upper)

# 4. 特征标准化
scaler = StandardScaler()
data_scaled = pd.DataFrame(
    scaler.fit_transform(data_filled),
    columns=data_filled.columns
)

# 5. 保存数据
data_scaled.to_csv('预处理后的数据.csv', index=False)
```

---

## ⚠️ 重要提醒

### 训练集和测试集分离

```python
from sklearn.model_selection import train_test_split

# 1. 先分割数据
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 2. 在训练集上fit
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)  # fit + transform

# 3. 在测试集上只transform（不要fit！）
X_test_scaled = scaler.transform(X_test)  # 只transform
```

### 常见错误

❌ **错误做法**:
```python
# 不要对测试集单独fit！
X_test_scaled = StandardScaler().fit_transform(X_test)  # 错误！
```

✅ **正确做法**:
```python
# 使用训练集的scaler
X_test_scaled = scaler.transform(X_test)  # 正确！
```

---

## 🎯 C题常见场景

### 场景1: 用户行为数据

**特点**: 有缺失值，量纲差异大

**处理流程**:
1. KNN填充缺失值
2. IQR法处理异常值
3. Z-score标准化

### 场景2: 金融数据

**特点**: 异常值多，分布偏斜

**处理流程**:
1. 中位数填充缺失值
2. Isolation Forest检测异常
3. Robust标准化

### 场景3: 传感器数据

**特点**: 时间序列，偶有异常

**处理流程**:
1. 前向填充缺失值
2. 3σ法检测异常
3. Min-Max归一化

---

## 📚 参考资料

- [Scikit-learn预处理文档](https://scikit-learn.org/stable/modules/preprocessing.html)
- [Pandas数据清洗指南](https://pandas.pydata.org/docs/user_guide/missing_data.html)

---

**祝你的数据预处理顺利！🎯**

