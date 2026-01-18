# 算法使用参考手册

快速查找美赛常用算法的使用方法。

## 📊 评价决策类

### 1. AHP（层次分析法）

**适用场景**：多准则决策问题
**美赛出现率**：⭐⭐⭐⭐⭐

```python
from algorithms.evaluation import AHP

ahp = AHP()

# 构建判断矩阵（示例：比较3个因素）
matrix = np.array([
    [1,   3,   5],    # 因素1相对重要性
    [1/3, 1,   2],    # 因素2相对重要性
    [1/5, 1/2, 1]     # 因素3相对重要性
])

# 计算权重
weights = ahp.calculate_weights(matrix)

# 一致性检验
cr = ahp.consistency_ratio(matrix)
if cr < 0.1:
    print("通过一致性检验")
```

**判断矩阵标度**：
- 1：同等重要
- 3：稍微重要
- 5：明显重要
- 7：强烈重要
- 9：极端重要

### 2. 熵权法（EWM）

**适用场景**：客观赋权
**美赛出现率**：⭐⭐⭐⭐⭐

```python
from algorithms.evaluation import EntropyWeight

ewm = EntropyWeight()

# 数据矩阵（m个样本，n个指标）
data = np.array([...])

# 计算权重
weights = ewm.calculate_weights(data)
```

### 3. TOPSIS

**适用场景**：多目标决策、方案排序
**美赛出现率**：⭐⭐⭐⭐

```python
from algorithms.evaluation import TOPSIS

topsis = TOPSIS()

# 决策矩阵
data = np.array([...])
weights = np.array([...])
is_benefit = [True, True, False, True]  # 指标类型

# 评价
scores, ranks = topsis.evaluate(data, weights, is_benefit)
```

### 4. 主客观组合权重

```python
from algorithms.evaluation import combined_weight

# AHP主观权重
subjective_w = ahp.calculate_weights(matrix)

# 熵权法客观权重
objective_w = ewm.calculate_weights(data)

# 组合（alpha=0.5表示等权重）
final_weights = combined_weight(subjective_w, objective_w, alpha=0.5)
```

## 📈 预测类

### 1. ARIMA时间序列

**适用场景**：时间序列预测
**美赛出现率**：⭐⭐⭐⭐⭐

```python
from statsmodels.tsa.arima.model import ARIMA

# 建立ARIMA(p,d,q)模型
model = ARIMA(data, order=(1, 1, 1))
fitted = model.fit()

# 预测
forecast = fitted.forecast(steps=10)

# 查看参数
print(fitted.summary())
```

**参数选择**：
- p：自回归阶数（ACF图）
- d：差分次数（平稳性检验）
- q：移动平均阶数（PACF图）

### 2. 灰色预测GM(1,1)

**适用场景**：小样本预测
**美赛出现率**：⭐⭐⭐

```python
# 基本GM(1,1)模型
def grey_model(x0, n_predict=5):
    n = len(x0)
    x1 = np.cumsum(x0)  # 一次累加
    
    # 构造数据矩阵
    B = np.zeros((n-1, 2))
    Y = x0[1:].reshape((n-1, 1))
    
    for i in range(n-1):
        B[i][0] = -(x1[i] + x1[i+1]) / 2
        B[i][1] = 1
    
    # 最小二乘估计
    a = np.linalg.inv(B.T @ B) @ B.T @ Y
    
    # 预测
    # ...（详细实现见algorithms模块）
```

## 🎯 优化类

### 1. 线性规划

**适用场景**：资源分配、生产计划
**美赛出现率**：⭐⭐⭐⭐

```python
from scipy.optimize import linprog

# 目标函数系数（求最小值）
c = [1, 2]

# 不等式约束 Ax <= b
A_ub = [[-1, 1], [1, 2]]
b_ub = [1, 4]

# 等式约束 Ax = b
A_eq = [[1, 1]]
b_eq = [3]

# 求解
result = linprog(c, A_ub=A_ub, b_ub=b_ub, 
                 A_eq=A_eq, b_eq=b_eq)
```

### 2. 非线性规划

```python
from scipy.optimize import minimize

# 目标函数
def objective(x):
    return x[0]**2 + x[1]**2

# 约束
constraints = [
    {'type': 'ineq', 'fun': lambda x: x[0] + x[1] - 1}
]

# 初始值
x0 = [0, 0]

# 求解
result = minimize(objective, x0, constraints=constraints)
```

### 3. 遗传算法

**适用场景**：复杂优化问题
**美赛出现率**：⭐⭐⭐⭐

```python
# 推荐使用 DEAP 或 PyGAD 库
from pygad import pygad

def fitness_func(solution, solution_idx):
    # 定义适应度函数
    return ...

ga_instance = pygad.GA(
    num_generations=100,
    num_parents_mating=4,
    fitness_func=fitness_func,
    sol_per_pop=50,
    num_genes=len(initial_solution)
)

ga_instance.run()
```

## 🤖 机器学习类

### 1. K-means聚类

**适用场景**：数据分组、客户细分
**美赛出现率**：⭐⭐⭐⭐

```python
from sklearn.cluster import KMeans

# 建立模型
kmeans = KMeans(n_clusters=3, random_state=42)

# 训练
kmeans.fit(data)

# 预测
labels = kmeans.predict(data)

# 聚类中心
centers = kmeans.cluster_centers_
```

### 2. 随机森林

**适用场景**：分类、回归、特征重要性
**美赛出现率**：⭐⭐⭐⭐

```python
from sklearn.ensemble import RandomForestClassifier

# 建立模型
rf = RandomForestClassifier(n_estimators=100, random_state=42)

# 训练
rf.fit(X_train, y_train)

# 预测
y_pred = rf.predict(X_test)

# 特征重要性
importances = rf.feature_importances_
```

### 3. 主成分分析（PCA）

**适用场景**：降维、特征提取
**美赛出现率**：⭐⭐⭐

```python
from sklearn.decomposition import PCA

# 降到2维
pca = PCA(n_components=2)

# 拟合并转换
X_reduced = pca.fit_transform(X)

# 方差解释率
explained_var = pca.explained_variance_ratio_
```

## 📐 图论类

### 1. 最短路径（Dijkstra）

```python
import networkx as nx

# 创建图
G = nx.Graph()
G.add_weighted_edges_from([
    (1, 2, 4), (1, 3, 2), (2, 3, 1), (2, 4, 5), (3, 4, 8)
])

# 最短路径
path = nx.shortest_path(G, source=1, target=4, weight='weight')
length = nx.shortest_path_length(G, source=1, target=4, weight='weight')
```

### 2. 最大流

```python
# 最大流问题
flow_value, flow_dict = nx.maximum_flow(G, source, sink)
```

## 🎲 仿真类

### 1. 蒙特卡洛模拟

**适用场景**：不确定性分析、风险评估
**美赛出现率**：⭐⭐⭐⭐

```python
import numpy as np

# 示例：估算π
n_simulations = 100000
x = np.random.uniform(-1, 1, n_simulations)
y = np.random.uniform(-1, 1, n_simulations)

# 计算落在圆内的点
inside_circle = (x**2 + y**2) <= 1
pi_estimate = 4 * np.sum(inside_circle) / n_simulations
```

## 📊 可视化

### 常用图表

```python
from data_analysis.visualization.plots import *

# 1. 时间序列图
plot_time_series(x, y, title="...", xlabel="...", ylabel="...")

# 2. 对比柱状图
plot_comparison(data_dict, title="...", ylabel="...")

# 3. 热力图
plot_heatmap(matrix, xticklabels, yticklabels, title="...")

# 4. 灵敏度分析图（美赛必备！）
plot_sensitivity_analysis(param_range, results, 
                         parameter_name="...", result_name="...")

# 5. 雷达图
plot_radar(data_dict, title="...")
```

## 💡 使用建议

### 算法选择原则

1. **评价决策类问题**：
   - 首选：AHP + 熵权法 + TOPSIS
   - 备选：模糊综合评价、灰色关联

2. **预测类问题**：
   - 首选：ARIMA、LSTM
   - 备选：灰色预测、回归分析

3. **优化类问题**：
   - 简单：线性规划
   - 复杂：遗传算法、模拟退火

4. **数据分析类**：
   - 聚类：K-means
   - 分类：随机森林、SVM
   - 降维：PCA

### 美赛建模技巧

1. **模型不要太复杂**：复杂模型容易止步M奖
2. **多做检验**：灵敏度分析、稳定性分析越多越好
3. **可视化重要**：图表要精美、清晰、专业
4. **假设要充分**：说明合理性和必要性
5. **创新可容错**：有创新即使有小错误也可能获奖

---

**更多示例代码请查看 `notebooks/examples/` 目录**

