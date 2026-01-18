# 美赛团队协作完全指南

> 以C题（大数据类）为例，详细说明三人团队的分工、工具配置和协作流程

## 📋 目录

1. [团队角色定位](#团队角色定位)
2. [工具环境配置](#工具环境配置)
3. [协作流程详解](#协作流程详解)
4. [五天时间轴](#五天时间轴)
5. [衔接关键点](#衔接关键点)

---

## 团队角色定位

### 🎯 建模手（Model Designer）

#### 主要职责
- 理解问题需求，拆解建模目标
- 选择合适的模型和算法
- 设计模型框架和逻辑
- 验证模型可行性
- 撰写模型推导部分

#### 需要掌握的技能
1. **数学建模基础**
   - 常见模型类型（评价、预测、优化）
   - 模型选择原则
   - 假设提出与合理性分析

2. **C题高频模型**（必须熟悉至少3-4个）
   - 时间序列：ARIMA、LSTM
   - 机器学习：随机森林、XGBoost、K-means
   - 回归分析：线性回归、逻辑回归
   - 深度学习：神经网络基础

3. **模型验证方法**
   - 评价指标（R²、RMSE、MAE、准确率等）
   - 交叉验证
   - 灵敏度分析

4. **文献检索能力**
   - 快速查找相关论文
   - 了解领域最新方法
   - 参考O奖论文的模型选择

#### 需要使用的工具
- **模型验证工具**：SPSSPRO（快速验证）、Python scikit-learn
- **AI辅助**：ChatGPT/Claude（查询"C题 预测 最优模型"）
- **文献工具**：Google Scholar、知网、百度学术
- **笔记工具**：Markdown编辑器（VSCode、Typora）

#### 工作输出
- 模型选择方案文档
- 模型框架图
- 数学推导过程
- 模型假设列表
- 参数设置建议

---

### 💻 编程手（Programmer）

#### 主要职责
- 实现建模手设计的模型
- 数据获取、清洗和预处理
- 模型训练和参数调优
- 生成计算结果和图表
- 代码优化和调试

#### 需要掌握的技能
1. **Python编程**（必须）
   - NumPy、Pandas数据处理
   - Matplotlib、Seaborn可视化
   - Scikit-learn机器学习
   - TensorFlow/PyTorch深度学习（可选）

2. **数据处理流程**
   - 数据清洗（缺失值、异常值处理）
   - 特征工程（标准化、归一化）
   - 数据划分（训练集、测试集）

3. **模型实现能力**
   - 能快速找到并改写现成代码
   - 调用主流库实现模型
   - 参数调优技巧

4. **可视化技能**
   - 绘制预测曲线、散点图
   - 绘制误差分析图、混淆矩阵
   - 绘制聚类结果、热力图

5. **Git版本控制**（重要！）
   - 代码提交与回滚
   - 分支管理
   - 团队协作

#### 需要使用的工具

##### 核心开发工具
- **Python环境**：Anaconda（推荐）
- **IDE**：VSCode / PyCharm / Jupyter Lab
- **版本控制**：Git + GitHub

##### Python核心库
```bash
# 必装
pip install numpy pandas matplotlib seaborn
pip install scikit-learn scipy statsmodels
pip install jupyter notebook

# 深度学习（可选）
pip install tensorflow  # 或 pytorch

# 数据获取
pip install requests beautifulsoup4 pandas-datareader

# 优化工具
pip install pulp cvxpy
```

##### VSCode插件配置
```
必装插件：
- Python（Microsoft官方）
- Pylance（代码补全）
- Jupyter（支持.ipynb）
- GitLens（Git可视化）

推荐插件：
- Code Runner（快速运行代码）
- Markdown All in One（写文档）
- Error Lens（实时显示错误）
```

##### Git配置（团队协作必备）
```bash
# 初始化仓库（第一次）
cd MathModelHub
git init
git config user.name "YourName"
git config user.email "your@email.com"

# 日常工作流
git add .                    # 添加所有修改
git commit -m "完成第一问代码"  # 提交说明
git push origin main         # 推送到远程（团队共享）

# 拉取队友更新
git pull origin main         # 获取最新代码
```

#### 工作输出
- 可运行的Python代码
- 处理后的数据文件
- 计算结果（CSV/Excel）
- 各类图表（PNG/PDF，300 DPI）
- 代码说明文档

---

### ✍️ 写作手（Writer）

#### 主要职责
- 撰写论文所有文字部分
- 绘制逻辑流程图、框架图
- 论文排版和美化
- 翻译和语法检查
- 最终论文整合

#### 需要掌握的技能
1. **LaTeX排版**（强烈推荐）
   - 基本语法
   - 公式编写
   - 图表插入
   - 参考文献管理

2. **论文结构设计**
   - 摘要写作（最重要！）
   - 引言、文献综述
   - 问题分析、模型描述
   - 结果分析、结论建议

3. **英文写作**
   - 学术英语表达
   - 避免中式英语
   - 使用连接词和过渡句

4. **图表绘制**
   - 流程图、框架图（非数据图）
   - 模型示意图
   - 逻辑关系图

5. **翻译技巧**
   - 使用翻译工具
   - 润色和校对
   - 专业术语准确性

#### 需要使用的工具

##### LaTeX环境配置

> 📚 **详细教程**：查看 `templates/07_README.md` 获取完整的LaTeX配置和使用教程  
> 📋 **速查表**：查看 `templates/08_LATEX_CHEATSHEET.md` 快速查找LaTeX命令

```bash
# 方案1：在线编辑器（推荐新手）⭐
- Overleaf（https://overleaf.com）
  优点：免费、无需配置、实时预览、团队协作
  模板位置：templates/latex/mcmthesis/
  
# 方案2：本地环境（推荐熟手）
- MacTeX（Mac）/ MiKTeX（Windows）
- VSCode + LaTeX Workshop插件
  详细配置见 templates/07_README.md
```

##### VSCode LaTeX配置
```json
推荐插件：
- LaTeX Workshop（必装）
- LaTeX Utilities（辅助）
- Spell Right（拼写检查）

LaTeX Workshop配置：
1. 安装插件后自动检测TeX环境
2. Ctrl/Cmd + S 保存时自动编译
3. 点击PDF预览实时查看
```

##### 翻译工具
- **DeepL**（推荐）：https://www.deepl.com
- **ChatGPT**：学术润色、改写
- **Grammarly**：语法检查（浏览器插件）
- **QuillBot**：改写工具

##### 画图工具
- **流程图**：
  - Draw.io（https://app.diagrams.net，免费）
  - ProcessOn（国内，免费）
  - Visio（专业）
  
- **模型框架图**：
  - PowerPoint（简单快速）
  - Inkscape（矢量图，免费）
  - Adobe Illustrator（专业）

- **数学公式**：
  - LaTeX内置
  - MathType（Word）
  - Online LaTeX Equation Editor

##### Git协作（论文版本管理）
```bash
# 论文也要用Git管理！
git add paper/main.tex
git commit -m "完成摘要初稿"
git push

# 避免冲突：每次开始写作前先拉取
git pull origin main
```

#### 工作输出
- 完整的LaTeX论文源码
- 所有流程图、框架图（矢量格式）
- 翻译后的英文稿
- 最终PDF论文

---

## 工具环境配置

### 全员必备

#### 1. Git团队协作配置

**为什么需要Git？**
- 防止代码/论文丢失
- 实时同步团队进度
- 版本回滚（出错时恢复）
- 避免文件冲突

自编参考文档：
[tools-git](https://notes.jiangxu.net/Misc/tools/git.html)
**配置步骤：**

```bash
# Step 1: 安装Git
# Mac: 已预装
# Windows: 下载 https://git-scm.com，自己网上搜教程

# Step 2: 配置身份
git config --global user.name "你的名字"
git config --global user.email "你的邮箱"

# Step 3: 创建GitHub/Gitee仓库（队长操作）
# 在GitHub创建私有仓库 MathModelHub
# 邀请队友为协作者

# Step 4: 克隆仓库到本地（所有人）
git clone https://github.com/yourteam/MathModelHub.git
cd MathModelHub

# Step 5: 日常协作命令
git status                # 查看修改状态
git add .                 # 添加所有修改
git commit -m "说明"       # 提交修改
git pull                  # 拉取队友更新（先拉取！）
git push                  # 推送到远程

# Step 6: 冲突处理（如果出现）
# 手动编辑冲突文件，保留正确内容
git add .
git commit -m "解决冲突"
git push
```

**协作规范：**
1. ⚠️ **每次开始工作前先 `git pull`**
2. ⚠️ **完成一个小任务就提交一次**
3. ⚠️ **commit信息要清楚**（如"完成第一问代码"）
4. ⚠️ **不要提交大文件**（>100MB用Git LFS）

#### 2. 团队沟通工具(可选)

- **腾讯会议/飞书会议**：全程连麦
- **微信群/钉钉群**：快速沟通
- **共享文档**：
  - 腾讯文档（实时协作）
  - 石墨文档
  - Notion（推荐，功能强大）

#### 3. 文件共享

- **坚果云/百度网盘**：备份论文和数据
- **GitHub仓库**：代码和LaTeX源文件
- **Overleaf**：LaTeX多人协作

---

### 编程手专属配置

#### Python开发环境

```bash
# 1. 安装Anaconda（推荐）
# 下载：https://www.anaconda.com/download

# 2. 创建虚拟环境（隔离项目）
conda create -n mcm python=3.10
conda activate mcm

# 3. 安装必备库
pip install -r requirements.txt

# 或手动安装
pip install numpy pandas matplotlib seaborn scikit-learn scipy statsmodels jupyter
```

#### VSCode完整配置

```json
// settings.json（VSCode设置）
{
    "python.defaultInterpreterPath": "/path/to/anaconda/envs/mcm/bin/python",
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true,
    "python.formatting.provider": "black",
    "editor.formatOnSave": true,
    "files.autoSave": "afterDelay",
    "files.autoSaveDelay": 1000
}
```

**必装VSCode插件列表：**
```
- Python（Microsoft）
- Pylance
- Jupyter
- GitLens
- Code Runner
- Error Lens
- autoDocstring（自动生成文档）
- Better Comments（注释高亮）
```

---

### 写作手专属配置

#### LaTeX环境（两种方案）

**方案1：VSCode本地环境（强烈推荐）⭐⭐⭐**

**为什么推荐本地环境？**
```
✅ 完全离线，编译速度快
✅ 与Git完美集成，协作方便
✅ 功能强大（自动补全、实时预览）
✅ 完全免费，无任何限制
✅ 比赛时更稳定（不依赖网络）
```

**安装步骤：**
```bash
# Mac安装（约4GB，需20-30分钟）
brew install --cask mactex
# 或下载 http://www.tug.org/mactex/

# Windows安装
# 下载 MiKTeX: https://miktex.org/download
# 安装时选择"Install missing packages on-the-fly: Yes"

# VSCode配置
1. 安装插件：LaTeX Workshop
2. 编译快捷键：
   - Ctrl/Cmd + Alt + B: 编译
   - Ctrl/Cmd + Alt + V: 预览PDF
```

**详细配置：** 见 `templates/07_README.md`

---

**方案2：Overleaf在线（备选，不推荐）**

**⚠️ 不推荐原因：**
```
❌ 免费版有严格限制（编译超时）
❌ 3人协作需要付费升级
❌ 需要稳定网络，断网无法工作
❌ 大项目编译很慢
```

**如果实在需要用：**
```
1. 注册 https://overleaf.com（用学校邮箱）
2. 创建新项目，上传MCM模板
3. 建议：仅作为备份，主环境用VSCode本地
```

#### 翻译工具配置

```
1. DeepL（必备）
   - 网页版：https://www.deepl.com
   - 客户端：更方便（推荐）
   - 每次翻译整段，不要逐句

2. ChatGPT润色
   提示词：
   "请将以下中文翻译成学术英语，用于数学建模论文：
   [你的中文]"

3. Grammarly浏览器插件
   - 安装后自动检查语法
   - 在VSCode和Overleaf中都能用
```

---

## 协作流程详解

### C题核心流程（大数据/预测类）

#### 阶段1：模型选择（Day 1下午，建模手主导）

**建模手工作流：**

```
1. 拆解题目需求
   ├─ 识别问题类型（预测？分类？聚类？）
   ├─ 明确评价指标（准确率？R²？）
   └─ 确定数据类型（时间序列？横截面？）

2. 选择候选模型（2-3个）
   ├─ 查阅O奖论文：past_problems/下找类似题目
   ├─ AI辅助：问ChatGPT "C题 预测趋势 最佳模型"
   └─ 参考本项目：docs/06_algorithms_reference.md

3. 快速验证可行性
   ├─ 用SPSSPRO跑小样本数据
   ├─ 评估R²/准确率是否合理
   └─ 确认代码包是否有现成实现

4. 确定最终方案
   ├─ 主模型：如LSTM（深度学习，适合时序）
   ├─ 对比模型：如ARIMA（经典，易解释）
   └─ 输出：模型选择文档 + 框架图
```

**与编程手衔接：**
- ⚠️ 确认模型后立即告知编程手
- ⚠️ 提供参考代码链接（GitHub/论文）
- ⚠️ 说明参数设置建议

**与写作手衔接：**
- ⚠️ 提供模型逻辑框架
- ⚠️ 解释模型选择理由
- ⚠️ 列出关键假设

---

#### 阶段2：代码实现（Day 2-3，编程手主导）

**编程手工作流：**

```
1. 数据获取与预处理
   ├─ 读取数据：pandas.read_csv()
   ├─ 探索性分析：describe(), info(), head()
   ├─ 数据清洗：
   │   ├─ 缺失值：dropna() / fillna()
   │   ├─ 异常值：3σ原则 / IQR
   │   └─ 重复值：drop_duplicates()
   └─ 特征工程：
       ├─ 标准化：StandardScaler
       ├─ 归一化：MinMaxScaler
       └─ 特征选择：相关性分析

2. 模型实现（套用现成代码）
   ├─ 找代码：GitHub搜索 "LSTM time series prediction"
   ├─ 改写：替换数据、调整参数
   └─ 调试：确保能跑通

3. 模型训练与验证
   ├─ 划分数据集：train_test_split(test_size=0.2)
   ├─ 训练模型：model.fit()
   ├─ 评估：计算R², RMSE, MAE
   └─ 调优：网格搜索 / 手动调参

4. 生成结果和图表
   ├─ 预测结果：保存为CSV
   ├─ 数据类图表（编程手负责）：
   │   ├─ 预测曲线：plot_time_series()
   │   ├─ 误差分析图：残差图、QQ图
   │   ├─ 聚类散点图：scatter plot
   │   └─ 热力图、混淆矩阵等
   └─ 保存：300 DPI PNG/PDF
```

**代码模板示例（LSTM预测）：**

```python
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
import matplotlib.pyplot as plt

# 1. 数据加载
data = pd.read_csv('data.csv')
values = data['value'].values.reshape(-1, 1)

# 2. 数据标准化
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(values)

# 3. 创建时间序列数据集
def create_dataset(data, look_back=10):
    X, y = [], []
    for i in range(len(data) - look_back):
        X.append(data[i:i+look_back])
        y.append(data[i+look_back])
    return np.array(X), np.array(y)

X, y = create_dataset(scaled_data)

# 4. 划分训练集和测试集
split = int(0.8 * len(X))
X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]

# 5. 构建LSTM模型
model = Sequential([
    LSTM(50, activation='relu', input_shape=(X_train.shape[1], 1)),
    Dense(1)
])
model.compile(optimizer='adam', loss='mse')

# 6. 训练
history = model.fit(X_train, y_train, epochs=100, 
                    validation_split=0.2, verbose=0)

# 7. 预测
predictions = model.predict(X_test)
predictions = scaler.inverse_transform(predictions)

# 8. 可视化
plt.figure(figsize=(12, 6))
plt.plot(y_test, label='Actual')
plt.plot(predictions, label='Predicted')
plt.legend()
plt.savefig('prediction.png', dpi=300, bbox_inches='tight')
```

**与建模手衔接：**
- ⚠️ 遇到问题及时沟通（模型跑不通、效果差）
- ⚠️ 同步训练进度和初步结果
- ⚠️ 确认评价指标是否符合预期

**与写作手衔接：**
- ⚠️ 第一问结果出来立即同步
- ⚠️ 提供结果数据（CSV）和图表（PNG）
- ⚠️ 解释图表含义和关键发现

---

#### 阶段3：论文撰写（Day 2-4，写作手主导）

**写作手工作流：**

```
1. Day 2上午：画逻辑框架图（不等代码）
   ├─ 整体流程图：数据→预处理→模型→结果
   ├─ 模型框架图：LSTM结构示意图
   └─ 使用Draw.io / PPT绘制

2. Day 2上午-下午：撰写前置部分
   ├─ 引言（Introduction）
   │   ├─ 问题背景：为什么重要？
   │   ├─ 文献综述：前人做了什么？
   │   └─ 论文结构：We organize...
   ├─ 问题重述（Restatement）
   │   └─ 用自己的话重新表述题目
   └─ 假设（Assumptions）
       └─ 建模手提供，写作手润色

3. Day 2下午-Day 3：边做边写
   ├─ 收到第一问结果→立即写第一问
   ├─ 模型描述：
   │   ├─ 为什么选这个模型？
   │   ├─ 模型公式和原理
   │   └─ 参数设置说明
   └─ 结果分析：
       ├─ 描述图表（Figure X shows...）
       ├─ 解释趋势和规律
       └─ 回答问题

4. Day 4上午：完成所有问题
   ├─ 确保每个问题都有结论
   ├─ 模型检验：
   │   ├─ 灵敏度分析（重要！）
   │   ├─ 稳定性分析
   │   └─ 误差分析
   └─ 结论与建议

5. Day 4下午：翻译与润色
   ├─ 使用DeepL整段翻译
   ├─ ChatGPT润色：
   │   "请润色以下学术英语段落：..."
   ├─ Grammarly检查语法
   └─ 团队互相检查

6. Day 4晚上：摘要（最后写！）
   ├─ 问题是什么？（1-2句）
   ├─ 我们做了什么？（3-4句）
   │   ├─ 提到主要模型
   │   ├─ 提到关键方法
   │   └─ 提到创新点
   ├─ 结论是什么？（2-3句）
   │   └─ 量化结果
   └─ 建议是什么？（1-2句）
```

**逻辑类图表（写作手负责）：**
- 整体流程图
- 模型框架图
- 问题分析图
- 层次结构图

**摘要写作模板：**

```
[Problem]
We address the problem of [具体问题]. This is important because [重要性].

[Approach]
To solve this, we develop a [模型名称] model that [做什么]. Specifically, we:
- First, we [步骤1]
- Then, we [步骤2] using [方法]
- Finally, we [步骤3]

Our model incorporates [创新点/特色].

[Results]
Our results show that [关键发现1]. Specifically, [具体数据]. We also find that [关键发现2], with [量化结果].

[Recommendations]
Based on our analysis, we recommend [建议1] and [建议2]. These recommendations will [效果].

Keywords: [关键词3-5个]
```

---

## 五天时间轴

### Day 1（选题日）- 全员协作

| 时间 | 建模手 | 编程手 | 写作手 |
|------|--------|--------|--------|
| **7:00-9:30** | 读题，记录每题思路 | 读题，评估数据可得性 | 读题，评估写作难度 |
| **9:30-10:00** | 讨论：排除无思路题目，留下1-2个候选 |
| **10:00-12:00** | 查文献，评估模型可行性 | 查GitHub，评估代码可得性 | 查O奖论文，评估写作难度 |
| **12:00** | **确定最终选题（C题）** |
| **14:00-15:30** | 拆解问题，列出建模目标 | 查找数据来源 | 阅读类似O奖论文 |
| **15:30-18:00** | 选择候选模型（2-3个） | 下载数据，探索性分析 | 创建LaTeX项目，写论文大纲 |
| **18:00-20:00** | 确定第一问模型（如LSTM） | 数据预处理，完成清洗 | 撰写引言、问题重述 |
| **20:00-22:00** | 撰写模型推导 | 搭建模型框架（不训练） | 画整体流程图 |

**Day 1关键衔接点：**
- ⚠️ 18:00前必须确定第一问模型
- ⚠️ 建模手要告诉编程手参考代码链接
- ⚠️ 建模手要给写作手模型逻辑框架

---

### Day 2（攻坚日）- 并行推进

| 时间 | 建模手 | 编程手 | 写作手 |
|------|--------|--------|--------|
| **8:00-12:00** | 完成第二问建模 | 训练第一问模型 | 撰写假设、问题分析 |
| **12:00** | ✅ 第一问模型推导完成 | ✅ 第一问结果输出 | 收到第一问结果 |
| **14:00-18:00** | 设计第三问模型 | 优化第一问，开始第二问 | 撰写第一问模型描述和结果 |
| **18:00-22:00** | 完成第三问建模 | 第二问代码实现 | 完成第一问全部内容 |

**Day 2关键衔接点：**
- ⚠️ 12:00 第一问结果必须出来
- ⚠️ 编程手要同步给写作手：结果CSV + 图表PNG
- ⚠️ 写作手要问清楚图表含义

---

### Day 3（冲刺日）- 加速完成

| 时间 | 建模手 | 编程手 | 写作手 |
|------|--------|--------|--------|
| **8:00-12:00** | 辅助编程手调试 | 完成第二问 | 撰写第二问内容 |
| **12:00** | ✅ 所有建模完成 | ✅ 第二问结果输出 | 收到第二问结果 |
| **14:00-18:00** | 做灵敏度分析 | 完成第三问 | 完成第二问撰写 |
| **18:00-22:00** | 撰写模型检验 | 做补充实验/画图 | 撰写第三问 |
| **22:00** | - | ✅ 所有问题代码完成 | - |

**Day 3关键衔接点：**
- ⚠️ 前三问中文稿必须完成
- ⚠️ 所有图表必须生成
- ⚠️ 所有数据结果必须确认

---

### Day 4（打磨日）- 翻译润色

| 时间 | 建模手 | 编程手 | 写作手 |
|------|--------|--------|--------|
| **8:00-12:00** | 检查模型逻辑 | 优化图表美观度 | 完成中文稿剩余部分 |
| **12:00** | ✅ 中文完整稿完成 |
| **14:00-18:00** | 辅助写摘要 | 补充灵敏度分析图 | 翻译（DeepL） |
| **18:00-22:00** | 检查英文模型部分 | 检查图表和数据 | 润色（ChatGPT） |
| **22:00-02:00** | 休息 | 休息 | 排版、调格式、写摘要 |

**Day 4关键衔接点：**
- ⚠️ 12:00前中文稿完成
- ⚠️ 摘要最后写（需要所有结果）
- ⚠️ 图表DPI必须300

---

### Day 5（提交日）- 最终检查

| 时间 | 全员任务 |
|------|---------|
| **8:00-9:00** | 交叉检查论文 |
| **9:00-9:30** | 修改发现的问题 |
| **9:30-10:00** | 生成最终PDF，提交！ |

**最终检查清单：**
```
□ 摘要完整（问题-方法-结果-建议）
□ 所有图表清晰（300 DPI）
□ 公式编号正确
□ 参考文献格式统一
□ 无语法错误（Grammarly检查）
□ 页数≤25页
□ PDF文件名正确
□ 控制编号填写正确
```

---

## 衔接关键点

### 1. 建模手 ↔ 编程手

**关键衔接点：**

| 时机 | 建模手输出 | 编程手需求 |
|------|-----------|-----------|
| 选题后 | 模型选择方案 | 确认代码包可得性 |
| 开始建模 | 模型框架、参考论文 | 找到参考代码 |
| 模型确定 | 数学公式、参数建议 | 实现代码 |
| 代码卡住 | 简化模型或换方案 | 反馈问题 |
| 结果异常 | 分析原因、调整模型 | 提供详细错误信息 |

**避免脱节：**
- ⚠️ 建模手选模型前问"有现成代码吗？"
- ⚠️ 编程手遇到问题立即反馈，不要死磕
- ⚠️ 不要选太复杂的模型（止步M奖）

**沟通方式：**
```
建模手：我准备用LSTM做时序预测，你看这个代码能用吗？
       [发GitHub链接]

编程手：可以，但这个代码需要TensorFlow 2.x
       我们环境是2.10，应该能跑

建模手：行，参数我建议用50个隐藏单元，学习率0.001

编程手：收到，我先跑一版看看效果
```

---

### 2. 编程手 ↔ 写作手

**关键衔接点：**

| 时机 | 编程手输出 | 写作手需求 |
|------|-----------|-----------|
| 数据预处理完成 | 数据描述统计 | 写数据来源和处理 |
| 第一问结果出 | 结果CSV + 图表PNG | 分析结果，撰写 |
| 每个问题完成 | 同步结果和图 | 立即写对应部分 |
| 画图时 | 确认图的含义 | 图题、图注怎么写 |
| 最终检查 | 所有数据和图 | 核对论文中的数字 |

**图表分工：**
- **编程手负责**：预测曲线、散点图、误差图、热力图等数据类图表
- **写作手负责**：流程图、框架图、示意图等逻辑类图表

**避免重复画图：**
```
编程手：这个预测曲线我已经画好了，在figures/prediction.png
写作手：好的，那模型框架图我来画

编程手：你需要聚类结果的散点图吗？参数可调
写作手：需要，最好用不同颜色区分簇，图例要清楚
```

**文件传递规范：**
```
figures/
├── q1_prediction.png       # 第一问预测图（编程手）
├── q1_error_analysis.png   # 误差分析（编程手）
├── model_framework.png     # 模型框架（写作手）
└── workflow.png            # 流程图（写作手）

results/
├── q1_predictions.csv      # 第一问结果
├── q2_clustering.csv       # 第二问结果
└── sensitivity_analysis.csv # 灵敏度分析
```

---

### 3. 建模手 ↔ 写作手

**关键衔接点：**

| 时机 | 建模手输出 | 写作手需求 |
|------|-----------|-----------|
| 模型选择 | 模型逻辑框架 | 画流程图 |
| 模型推导 | 数学公式、变量说明 | 写模型描述 |
| 假设提出 | 假设列表和理由 | 撰写假设部分 |
| 模型检验 | 灵敏度分析方法 | 写检验部分 |
| 写摘要 | 关键创新点 | 摘要突出亮点 |

**沟通方式：**
```
写作手：你这个模型为什么选LSTM不选ARIMA？
建模手：因为数据有非线性特征，LSTM能捕捉长期依赖
       论文里你可以写"考虑到时间序列的非线性和长期依赖性..."

写作手：灵敏度分析你做了哪些参数？
建模手：测试了学习率0.001, 0.01, 0.1，隐藏单元50, 100, 200
       结果表明学习率0.001时最稳定

写作手：好的我写进去
```

---

### 4. 全员协作要点

**每日站会（15分钟）：**
```
时间：每天早上9:00

内容：
- 昨天完成了什么？
- 今天计划做什么？
- 遇到什么困难？

示例：
建模手：昨天完成第一问建模，今天做第二问，需要编程手确认数据格式
编程手：昨天跑通第一问，今天优化和做第二问，没问题
写作手：昨天写了引言，今天写第一问，需要编程手同步结果
```

**实时沟通规范：**
```
✅ 好的沟通：
"第一问LSTM结果出来了，R²=0.92，图表在figures/q1.png"

❌ 不好的沟通：
"弄好了"（什么弄好了？在哪？）
```

**Git提交规范：**
```
# 清晰的commit message
git commit -m "完成第一问LSTM模型代码"
git commit -m "添加第一问预测曲线图"
git commit -m "完成论文引言和假设部分"

# 不好的commit
git commit -m "update"
git commit -m "修改"
```

---

## 常见问题处理

### Q1: 模型跑不出结果怎么办？

**建模手和编程手协作：**
1. 先简化模型（复杂→简单）
2. 检查数据预处理（最常见问题）
3. 调整参数（学习率、迭代次数）
4. 换备选模型（LSTM跑不通→用ARIMA）
5. **关键**：不要死磕，保证论文完整性

### Q2: 时间不够怎么办？

**优先级排序：**
1. 摘要（最重要！占分40%）
2. 论文完整性（有结论）
3. 图表质量
4. 模型复杂度
5. 语言润色

**应急策略：**
- 简化后面的问题
- 减少模型对比
- 用简单模型（线性回归也行）
- 保证前两问质量

### Q3: Git冲突怎么办？

**预防：**
- 每次工作前先 `git pull`
- 不同人改不同文件
- LaTeX用Overleaf（自动合并）

**解决：**
```bash
# 出现冲突时
git pull  # 会提示冲突文件

# 打开冲突文件，看到：
<<<<<<< HEAD
你的修改
=======
队友的修改
>>>>>>> branch

# 手动选择保留哪个，或合并
# 删除标记符号 <<<< ==== >>>>

git add 冲突文件
git commit -m "解决冲突"
git push
```

### Q4: 队友节奏不一致怎么办？

**建议：**
- 提前一周磨合
- 明确分工和deadline
- 每日站会同步进度
- 互相帮助（提前完成的帮忙检查）

---

## 工具速查表

### 建模手

| 任务 | 工具 |
|------|------|
| 模型选择 | O奖论文、ChatGPT、algorithms_reference.md |
| 快速验证 | SPSSPRO、Python scikit-learn |
| 文献检索 | Google Scholar、知网 |
| 笔记 | Markdown（VSCode/Typora） |

### 编程手

| 任务 | 工具 |
|------|------|
| Python环境 | Anaconda |
| IDE | VSCode + Python插件 |
| 版本控制 | Git + GitHub/Gitee |
| 数据处理 | NumPy, Pandas |
| 机器学习 | Scikit-learn, TensorFlow |
| 可视化 | Matplotlib, Seaborn |
| 调试 | Jupyter Notebook |

### 写作手

| 任务 | 工具 |
|------|------|
| LaTeX编辑 | Overleaf（在线）/ VSCode + LaTeX Workshop |
| 翻译 | DeepL, ChatGPT |
| 语法检查 | Grammarly |
| 流程图 | Draw.io, ProcessOn |
| 公式编辑 | LaTeX, MathType |
| 版本控制 | Git |

### 全员

| 任务 | 工具 |
|------|------|
| 版本控制 | Git |
| 沟通 | 腾讯会议、微信 |
| 文档协作 | 腾讯文档、Notion |
| 文件共享 | GitHub、坚果云 |

---

## 总结

### 成功的关键

1. **提前准备**：工具环境配置好（尤其Git！）
2. **明确分工**：各司其职，不越界不脱节
3. **实时沟通**：遇到问题立即反馈
4. **并行工作**：不要等前一步完成才开始
5. **保持节奏**：每日站会，确保同步

### 最重要的三句话

1. ⚠️ **Git先pull再push**（避免冲突）
2. ⚠️ **结果出来立即同步**（不要等）
3. ⚠️ **论文完整最重要**（不追求完美）

---

**祝你们团队协作顺利，美赛取得好成绩！🏆**

