## 工具函数模块

## 📁 文件列表

| 文件 | 功能 | 主要函数 |
|-----|------|---------|
| `数据读取工具.py` | 读取各种格式的数据文件 | CSV、Excel、JSON、SQL |
| `评估指标.py` | 模型性能评估 | 分类指标、回归指标、混淆矩阵 |
| `时间处理.py` | 日期时间数据处理 | 格式转换、特征提取、时间差计算 |

## 🚀 快速开始

### 1. 安装依赖
```bash
pip install pandas numpy scikit-learn matplotlib seaborn
```

### 2. 运行示例
```bash
cd data_analysis/utils

# 查看数据读取工具
python 数据读取工具.py

# 查看评估指标
python 评估指标.py

# 查看时间处理
python 时间处理.py
```

## 📊 功能详解

### 1. 数据读取工具.py

**支持的文件格式**:
- ✅ CSV文件 (`.csv`)
- ✅ Excel文件 (`.xlsx`, `.xls`)
- ✅ JSON文件 (`.json`)
- ✅ 数据库 (SQL)
- ✅ 文本文件 (`.txt`)

**主要函数**:
```python
from 数据读取工具 import read_file_auto, quick_preview

# 自动识别文件类型并读取
data = read_file_auto('data.csv')

# 快速查看数据信息
quick_preview(data, n_rows=10)
```

---

### 2. 评估指标.py

**分类任务**:
- 准确率 (Accuracy)
- 精确率 (Precision)
- 召回率 (Recall)
- F1分数 (F1-Score)
- 混淆矩阵 (Confusion Matrix)

**回归任务**:
- MSE (均方误差)
- RMSE (均方根误差)
- MAE (平均绝对误差)
- R² (决定系数)
- MAPE (平均绝对百分比误差)

**主要函数**:
```python
from 评估指标 import evaluate_classification, evaluate_regression

# 评估分类模型
metrics = evaluate_classification(y_true, y_pred, labels=['A', 'B', 'C'])

# 评估回归模型
metrics = evaluate_regression(y_true, y_pred)

# 绘制混淆矩阵
plot_confusion_matrix(y_true, y_pred, labels=['A', 'B', 'C'])

# 绘制回归结果
plot_regression_results(y_true, y_pred)
```

---

### 3. 时间处理.py

**日期时间处理**:
- 格式转换
- 特征提取（年、月、日、星期等）
- 时间差计算
- 日期范围生成
- 时间序列重采样

**主要函数**:
```python
from 时间处理 import extract_datetime_features, calculate_date_diff

# 从日期列提取特征
data = extract_datetime_features(data, '日期')

# 计算两个日期的差异
days = calculate_date_diff('2023-01-01', '2023-12-31', unit='days')

# 生成日期范围
dates = generate_date_range('2023-01-01', '2023-12-31', freq='D')

# 时间序列重采样
daily_data = resample_timeseries(hourly_data, '时间', freq='D', agg_func='mean')
```

---

## 💡 常见使用场景

### 场景1: 快速读取和预览数据

```python
from 数据读取工具 import read_file_auto, quick_preview

# 读取数据（自动识别格式）
data = read_file_auto('data.csv')

# 快速预览
quick_preview(data, n_rows=5)
```

### 场景2: 模型评估

```python
from 评估指标 import evaluate_classification, plot_confusion_matrix

# 训练模型后评估
y_pred = model.predict(X_test)

# 评估分类性能
metrics = evaluate_classification(y_test, y_pred)

# 可视化混淆矩阵
plot_confusion_matrix(y_test, y_pred, save_path='confusion_matrix.png')
```

### 场景3: 时间特征工程

```python
from 时间处理 import extract_datetime_features

# 从日期列提取多个时间特征
data = extract_datetime_features(data, '订单日期')

# 现在可以使用'订单日期_月', '订单日期_星期', '订单日期_是否周末'等特征
```

### 场景4: 时间序列分析

```python
from 时间处理 import resample_timeseries

# 将小时数据聚合为天数据
daily_data = resample_timeseries(
    hourly_data,
    datetime_column='时间',
    freq='D',  # 按天聚合
    agg_func='mean'  # 取平均值
)
```

---

## 🎯 C题常见应用

### 用户行为分析

```python
from 数据读取工具 import read_file_auto
from 时间处理 import extract_datetime_features

# 1. 读取用户行为数据
data = read_file_auto('user_behavior.csv')

# 2. 提取时间特征
data = extract_datetime_features(data, '访问时间')

# 3. 现在可以分析：
# - 哪个月份用户最活跃（'访问时间_月'）
# - 周末和工作日行为差异（'访问时间_是否周末'）
# - 哪个小时用户最活跃（'访问时间_小时'）
```

### 模型性能评估

```python
from 评估指标 import evaluate_classification, plot_confusion_matrix

# 对比多个模型
models = {'模型A': y_pred_a, '模型B': y_pred_b, '模型C': y_pred_c}

for model_name, y_pred in models.items():
    print(f"\n{model_name}:")
    metrics = evaluate_classification(y_test, y_pred, print_report=True)
    plot_confusion_matrix(y_test, y_pred, save_path=f'{model_name}_confusion.png')
```

---

## 📚 扩展阅读

- [Pandas官方文档](https://pandas.pydata.org/docs/)
- [Scikit-learn评估指标](https://scikit-learn.org/stable/modules/model_evaluation.html)
- [Python日期时间处理](https://docs.python.org/3/library/datetime.html)

---

**让数据分析更简单！📊**

