# 📚 新手路线图快速总结（按角色）

## 🎯 首先：确定你的角色

| 角色 | 主要职责 | 需要安装 | 查看详细 |
|------|---------|---------|---------|
| **👨‍🔬 建模手** | 模型设计、推导 | Git + Python | [详细路线](./02_BEGINNER_ROADMAP.md#建模手学习路线) |
| **💻 编程手** | 代码实现、求解 | Git + Python + 完整环境 | [详细路线](./02_BEGINNER_ROADMAP.md#编程手学习路线) |
| **✍️ 写作手** | 论文撰写、排版 | Git + LaTeX（**不需要Python**） | [详细路线](./02_BEGINNER_ROADMAP.md#写作手学习路线) |

---

## 📅 6周学习计划（按角色）

### 👨‍🔬 建模手

```
Week 1-2: Git基础 + 熟悉项目
Week 3-4: 学习算法（AHP、TOPSIS、熵权法）⭐
Week 5:   Python快速验证
Week 6:   团队磨合、模拟比赛
```

**重点：**
- ✅ 精通2-3个高频算法
- ✅ 能用Python验证即可（不需要精通编程）
- ✅ 阅读O奖论文学习建模思路

---

### 💻 编程手

```
Week 1:   Git基础 + Python基础（如不熟悉）
Week 2-3: NumPy、Pandas、Matplotlib⭐
Week 4:   算法实现（找代码、改代码）
Week 5:   Git协作演练
Week 6:   团队磨合、模拟比赛
```

**重点：**
- ✅ 熟练数据处理（NumPy、Pandas）
- ✅ 能快速找到并改写现成代码
- ✅ Git协作要非常熟练

---

### ✍️ 写作手

```
Week 1:   Git基础 + 阅读O奖论文
Week 2-3: LaTeX学习（VSCode + LaTeX Workshop）⭐
Week 4:   英文写作 + 翻译工具
Week 5:   流程图绘制 + Git协作
Week 6:   团队磨合、模拟比赛
```

**重点：**
- ✅ LaTeX基本操作（VSCode推荐，Overleaf备选）
- ✅ 摘要写作模板背熟（决定命运）
- ✅ **不需要安装Python**

---

## ⚡ 2周冲刺版

### 所有角色共同

**Week 1：**
```
Day 1-2: Git基础（必学）
Day 3-7: 根据角色学核心技能
```

**Week 2：**
```
Day 1-3: 团队磨合
Day 4-5: 模拟比赛
Day 6-7: 资料准备
```

### 按角色的核心技能

| 角色 | Week 1 核心技能（5天） |
|------|---------------------|
| 建模手 | AHP + TOPSIS |
| 编程手 | NumPy + Pandas |
| 写作手 | VSCode + LaTeX配置 |

---

## 📋 必学优先级（按角色）

### 👨‍🔬 建模手

**⭐⭐⭐ 必须掌握：**
1. Git基础操作
2. AHP（层次分析法）
3. TOPSIS / 熵权法
4. Python基础验证

**⭐⭐ 推荐掌握：**
1. ARIMA时间序列
2. 线性回归
3. 假设提出方法

**⭐ 可选：**
1. 深度学习（LSTM）
2. 复杂优化算法

---

### 💻 编程手

**⭐⭐⭐ 必须掌握：**
1. Git基础操作（要非常熟练）
2. NumPy、Pandas
3. Matplotlib可视化
4. 能找代码、改代码

**⭐⭐ 推荐掌握：**
1. scikit-learn基础
2. 数据清洗技巧
3. 代码调试能力

**⭐ 可选：**
1. 深度学习框架
2. 高级可视化

---

### ✍️ 写作手

**⭐⭐⭐ 必须掌握：**
1. Git基础操作
2. LaTeX基本操作（VSCode + LaTeX Workshop）
3. 摘要写作模板
4. 翻译工具使用

**⭐⭐ 推荐掌握：**
1. 流程图绘制
2. 常用学术表达
3. 英文润色技巧

**⭐ 可选：**
1. Overleaf在线环境（作为备选）
2. 高级排版技巧

---

## 🔧 工具安装清单

### 所有人必装

```
✅ Git
✅ GitHub账号
✅ VSCode
```

### 按角色安装

| 工具 | 建模手 | 编程手 | 写作手 |
|------|-------|-------|-------|
| **Python** | ✅ 需要 | ✅ 需要 | ❌ **不需要** |
| **Anaconda** | ⭕ 可选 | ✅ 推荐 | ❌ 不需要 |
| **LaTeX引擎** | ❌ 不需要 | ❌ 不需要 | ✅ **必需** |
| **VSCode LaTeX** | ❌ 不需要 | ❌ 不需要 | ✅ **推荐** |
| **Overleaf** | ❌ 不需要 | ❌ 不需要 | ⭕ 备选 |

---

## 🚀 今天就开始

### Step 1: 安装Git（所有人）

```bash
# Mac
git --version  # 检查是否已安装

# Windows
# 下载 https://git-scm.com/download/win

# 配置
git config --global user.name "你的名字"
git config --global user.email "你的邮箱"
```

### Step 2: 获取项目（所有人）

```bash
git clone https://github.com/Jaxon1216/MathModelHub.git
cd MathModelHub
```

### Step 3: 根据角色安装工具

**👨‍🔬 建模手：**
```bash
# 安装Python
# Mac: brew install python
# Windows: 下载 python.org

# 安装依赖
pip install -r requirements.txt
```

**💻 编程手：**
```bash
# 下载Anaconda
# 访问 anaconda.com/download

# 创建环境
conda create -n mcm python=3.10
conda activate mcm
pip install -r requirements.txt
```

**✍️ 写作手：**
```
# 安装LaTeX环境
Mac: brew install --cask mactex
Windows: 下载安装 MiKTeX (https://miktex.org)

# 安装VSCode插件
打开VSCode → Extensions → 搜索安装：LaTeX Workshop

# 打开模板
VSCode → File → Open Folder
→ 打开 templates/latex/mcmthesis/
→ 打开 mcmthesis-demo.tex
→ Ctrl/Cmd+Alt+B 编译查看

# 不需要安装Python！
# 详细配置见 templates/07_README.md
```

---

## 📖 文档阅读顺序

### 按经验水平

**完全新手：**
```
1. 本文（5分钟了解全局）
2. 02_BEGINNER_ROADMAP.md → 找到你的角色部分
3. 按角色的学习路径开始学习
```

**有基础：**
```
1. 01_QUICKSTART.md（快速上手）
2. docs/05_team_workflow.md（团队协作）
```

### 按角色

**👨‍🔬 建模手：**
```
02_BEGINNER_ROADMAP.md（建模手部分）
  ↓
docs/06_algorithms_reference.md（算法手册）
  ↓
past_problems/README.md（历年题型）
  ↓
docs/05_team_workflow.md（协作流程）
```

**💻 编程手：**
```
02_BEGINNER_ROADMAP.md（编程手部分）
  ↓
notebooks/examples/（运行示例）
  ↓
data_analysis/（查看工具）
  ↓
docs/05_team_workflow.md（协作流程）
```

**✍️ 写作手：**
```
02_BEGINNER_ROADMAP.md（写作手部分）
  ↓
templates/07_README.md（LaTeX教程）
  ↓
templates/08_LATEX_CHEATSHEET.md（速查表）
  ↓
docs/04_mcm_guide.md（论文写作技巧）
  ↓
docs/05_team_workflow.md（协作流程）
```

---

## ⚠️ 常见误区（按角色）

### 👨‍🔬 建模手

❌ **错误：**
- 想学完所有算法
- 纠结复杂模型
- 花太多时间学编程

✅ **正确：**
- 精通2-3个高频模型
- 重点学AHP、TOPSIS
- Python能验证就行

---

### 💻 编程手

❌ **错误：**
- 想从零写代码
- 追求代码完美
- 不学Git协作

✅ **正确：**
- 找现成代码改
- 能跑通就行
- Git要非常熟练

---

### ✍️ 写作手

❌ **错误：**
- 觉得需要学Python
- 等所有结果出来再写
- 不重视摘要

✅ **正确：**
- 只需Git + LaTeX
- 边做边写
- 摘要决定命运

---

## 🤝 团队协作核心

### 所有人必须掌握的Git命令

```bash
git pull        # 开始工作前（最重要！）
git add .
git commit -m "说明"
git push        # 及时推送
```

### 分工避免冲突

```
建模手：sections/model.tex（模型推导）
编程手：code/ + figures/（代码和图表）
写作手：main.tex（论文主体）
```

### 每日站会（15分钟）

```
9:00 开会：
- 昨天完成了什么
- 今天计划做什么
- 遇到什么困难
```

---

## 🎓 记住

### 对所有角色

- ✅ Git是所有人都必须学的
- ✅ 循序渐进，不要贪多
- ✅ 动手实践比看教程重要
- ✅ 团队协作比个人能力重要

### 对建模手

- ✅ 理论重于编程
- ✅ 精通2-3个模型就够
- ✅ Python只用于验证

### 对编程手

- ✅ 熟练数据处理
- ✅ 能快速找代码改代码
- ✅ Git要非常熟练

### 对写作手

- ✅ LaTeX是必须的
- ✅ 摘要决定命运（40%分数）
- ✅ **不需要Python**
- ✅ 论文完整比完美重要

---

## 📋 检查清单（打印备用）

### 建模手

```
□ Git安装并配置
□ Python环境可用
□ 能运行项目示例
□ AHP/TOPSIS熟练
□ 阅读过O奖论文
```

### 编程手

```
□ Git安装并配置
□ Python完整环境
□ NumPy/Pandas熟练
□ 能找代码改代码
□ Git协作熟练
```

### 写作手

```
□ Git安装并配置
□ VSCode + LaTeX环境配置完成
□ LaTeX基本操作熟练
□ 摘要模板背熟
□ 翻译工具准备好
□ (可选) Overleaf账号作为备选
```

---

**📚 详细内容查看：[02_BEGINNER_ROADMAP.md](./02_BEGINNER_ROADMAP.md)**

**🚀 立即开始：根据你的角色，查看对应章节！**
