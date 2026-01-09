# 🎓 新手完整学习路线图（按角色定制）

> 根据你的角色，选择对应的学习路径

## 🎯 首先：确定你的角色

美赛三人团队通常这样分工：

| 角色 | 主要职责 | 需要掌握 | 本文对应章节 |
|------|---------|---------|-------------|
| **👨‍🔬 建模手** | 模型设计、推导 | 数学+算法+Python验证 | [→ 建模手路线](#建模手学习路线) |
| **💻 编程手** | 代码实现、求解 | Python+Git+数据分析 | [→ 编程手路线](#编程手学习路线) |
| **✍️ 写作手** | 论文撰写、排版 | LaTeX+Git+英文写作 | [→ 写作手路线](#写作手学习路线) |

**💡 提示：**
- 分工不绝对，但每人要有侧重
- 建议提前1个月确定角色
- 可以一人兼多职，但要合理分配精力

---

## 📋 通用准备（所有人必做）

### Step 0: 安装Git（必需）⭐

**为什么所有人都需要Git？**
- 团队协作的核心工具
- 实时同步代码和论文
- 版本控制，防止丢失

#### Mac用户：
```bash
# 检查是否已安装
git --version

# 如未安装，使用Homebrew
brew install git
```

#### Windows用户：
```
1. 访问 https://git-scm.com/download/win
2. 下载并安装Git
3. 安装时选择默认选项
4. 验证：打开CMD，输入 git --version
```

#### 配置Git身份（必需）：
```bash
# 设置用户名和邮箱
git config --global user.name "你的名字"
git config --global user.email "你的邮箱@example.com"

# 验证配置
git config --global --list
```

### Step 1: 注册GitHub账号（必需）

```
1. 访问 https://github.com
2. 点击「Sign up」注册
3. 验证邮箱
4. 设置个人资料

💡 建议使用学校邮箱（可享受教育优惠）
```

### Step 2: 安装VSCode（推荐）

**下载：** https://code.microsoft.com/

**必装插件（所有人）：**
```
1. GitLens（Git可视化，必装）
2. Markdown All in One（编辑文档）
```

### Step 3: 获取本项目（必需）

```bash
# 创建工作目录
cd ~/Documents
mkdir code
cd code

# 克隆项目
git clone https://github.com/Jaxon1216/MathModelHub.git
cd MathModelHub

# 查看结构
ls -la
```

### Step 4: 学习Git基础（必需）⭐

**学习资源：**
```
1. 作者Git教程：
   https://notes.jiangxu.net/Misc/tools/git.html

2. B站搜索：「Git教程」
   推荐：尚硅谷/黑马程序员（2-3小时）

3. 在线练习：
   https://learngitbranching.js.org/?locale=zh_CN
```

**必须掌握的命令（所有人）：**
```bash
git status          # 查看状态
git pull            # 拉取更新（开始工作前必做）
git add .           # 添加修改
git commit -m "说明" # 提交修改
git push            # 推送到远程
git log             # 查看历史
```

**学习时间：** 2-3天

---

## 👨‍🔬 建模手学习路线

> 你负责：模型设计、数学推导、假设提出、模型验证

### 🎯 需要安装的工具

#### 必需工具：
```
✅ Git（已安装，见通用准备）
✅ VSCode（已安装）
✅ Python 3.8+（用于验证模型）
```

#### Python安装（用于快速验证）：

**Mac用户：**
```bash
# 使用Homebrew
brew install python

# 验证
python3 --version
```

**Windows用户：**
```
1. 访问 https://www.python.org/downloads/
2. 下载Python 3.10+
3. 安装时勾选「Add Python to PATH」
4. 验证：python --version
```

#### VSCode插件（建模手）：
```
1. Python（Microsoft官方）
2. Jupyter（运行notebook）
```

#### 安装项目依赖：
```bash
cd MathModelHub
pip install -r requirements.txt

# 或使用国内镜像
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

---

### 📚 学习路径（建模手）

#### 阶段1：熟悉项目（1-2天）

**必读文档：**
```
1. README.md（了解项目）
2. docs/04_mcm_guide.md（美赛评审机制）
3. docs/06_algorithms_reference.md（算法手册）⭐
4. past_problems/README.md（历年题型分析）
```

**实践任务：**
```bash
# 查看算法示例
cd notebooks/examples
python ahp_example.py
python topsis_example.py

# 理解输出结果
```

---

#### 阶段2：学习高频算法（2-3周）⭐ 核心

**Week 1：评价决策类（最重要）**

**必学模型（出现率>80%）：**
```
1. AHP（层次分析法）⭐⭐⭐
   - 原理：docs/06_algorithms_reference.md
   - 代码：algorithms/evaluation.py
   - 示例：notebooks/examples/ahp_example.py
   
   重点掌握：
   - 构建判断矩阵（1-9标度）
   - 计算权重
   - 一致性检验（CR<0.1）
   
2. 熵权法（EWM）⭐⭐⭐
   - 客观赋权方法
   - 常与AHP结合使用
   
3. TOPSIS⭐⭐⭐
   - 多目标决策
   - 方案排序
```

**学习方法：**
```
Day 1-2: 理解原理（看文档+视频）
Day 3-4: 看代码实现
Day 5-6: 修改参数实验
Day 7:   总结笔记
```

**Week 2：预测类（C题常用）**

**推荐模型：**
```
1. 线性回归⭐⭐
   - 最简单的预测方法
   - scikit-learn实现
   
2. ARIMA时间序列⭐⭐⭐
   - 趋势预测
   - statsmodels库
   
3. 灰色预测GM(1,1)⭐⭐
   - 小样本预测
```

**Week 3：优化规划类**

**了解即可：**
```
1. 线性规划
2. 非线性规划
3. 遗传算法（复杂，谨慎使用）
```

---

#### 阶段3：Python快速验证（1周）

**目标：** 能用Python快速验证模型可行性

**需要掌握（够用即可）：**
```python
# NumPy基础
import numpy as np
arr = np.array([1, 2, 3])
print(arr.mean(), arr.std())

# Pandas基础（读数据）
import pandas as pd
df = pd.read_csv('data.csv')
print(df.head())

# 可视化（调用项目工具）
from data_analysis.visualization.plots import *
plot_time_series(x, y, title="...")
```

**学习资源：**
```
B站搜索：「NumPy快速入门」（2-3小时）
B站搜索：「Pandas基础教程」（3-4小时）
```

**⚠️ 注意：** 建模手不需要精通编程，能验证即可！

---

#### 阶段4：实战准备（赛前1-2周）

**任务清单：**
```
□ 熟练掌握AHP、TOPSIS、熵权法
□ 能用Python快速验证模型
□ 阅读3-5篇O奖论文（past_problems/）
□ 了解假设提出的方法
□ 了解灵敏度分析的做法
□ 准备常用判断矩阵
□ Git协作练习
```

**模拟练习：**
```
选一道历年题目
1小时内：
- 拆解问题
- 提出假设
- 选择模型
- 画出框架图
```

---

### 💡 建模手要点

**你的核心价值：**
```
✅ 理解问题本质
✅ 选择合适模型
✅ 提出合理假设
✅ 设计验证方案
✅ 写模型推导部分
```

**不要纠结：**
```
❌ 复杂编程（交给编程手）
❌ 深度学习（容易止步M奖）
❌ 所有算法都学（时间不够）
```

**工作输出：**
```
- 模型选择方案文档
- 模型框架图
- 数学推导过程
- 假设列表
- 参数建议
```

---

## 💻 编程手学习路线

> 你负责：代码实现、数据处理、模型求解、图表绘制

### 🎯 需要安装的工具

#### 必需工具：
```
✅ Git（已安装）
✅ VSCode（已安装）
✅ Python 3.8+（必需）⭐
✅ Anaconda（推荐）
```

#### Python完整环境（必需）：

**推荐：使用Anaconda**
```
1. 访问 https://www.anaconda.com/download
2. 下载Anaconda（包含Python和常用库）
3. 安装后创建虚拟环境：

conda create -n mcm python=3.10
conda activate mcm
```

#### VSCode插件（编程手）：
```
必装：
1. Python（Microsoft官方）
2. Pylance（代码补全）
3. Jupyter（运行notebook）
4. GitLens（Git可视化）

推荐：
5. Code Runner（快速运行）
6. Error Lens（实时错误）
7. autoDocstring（文档生成）
```

#### 安装项目依赖（必需）：
```bash
cd MathModelHub
pip install -r requirements.txt

# 验证安装
python -c "import numpy, pandas, matplotlib; print('成功')"
```

---

### 📚 学习路径（编程手）

#### 阶段1：Python基础（如不熟悉，1周）

**如果Python基础薄弱：**
```
B站搜索：「Python零基础教程」
推荐：黑马程序员/尚硅谷
时长：看前20集即可（每集30-40分钟）

必须掌握：
- 变量、数据类型
- 列表、字典
- 循环、函数
- 文件读写
```

**如果有基础，跳过此阶段**

---

#### 阶段2：数据处理三件套（1-2周）⭐ 核心

**Week 1：NumPy & Pandas**

**NumPy（数组计算）：**
```python
import numpy as np

# 必须掌握
arr = np.array([1, 2, 3])
arr.mean(), arr.std()           # 统计
arr + 5                         # 广播
np.linspace(0, 10, 50)         # 生成数组
```

**Pandas（数据处理）：**
```python
import pandas as pd

# 必须掌握
df = pd.read_csv('data.csv')   # 读取
df.head()                       # 查看
df.describe()                   # 统计
df['col'].mean()                # 计算
df.dropna()                     # 清洗
```

**学习资源：**
```
B站搜索：「NumPy教程」（3-4小时）
B站搜索：「Pandas教程」（5-6小时）

实践：运行 notebooks/examples/ 下的所有例子
```

**Week 2：Matplotlib & Seaborn（可视化）**

**必须掌握：**
```python
import matplotlib.pyplot as plt
import seaborn as sns

# 基本图表
plt.plot(x, y)                 # 折线图
plt.scatter(x, y)              # 散点图
plt.bar(x, y)                  # 柱状图
sns.heatmap(data)              # 热力图

# 使用项目工具（推荐）
from data_analysis.visualization.plots import *
set_mcm_style()                # 设置美赛风格
plot_time_series(x, y, ...)
```

**学习资源：**
```
直接用项目提供的可视化工具
查看：data_analysis/visualization/plots.py
```

---

#### 阶段3：算法实现（2周）⭐ 核心

**任务：** 能快速实现建模手设计的模型

**学习方法：**
```
不要从零写代码！
✅ 先找现成代码（GitHub）
✅ 理解代码逻辑
✅ 改数据、调参数
✅ 确保能跑通
```

**必会算法库：**
```python
# scikit-learn（机器学习）
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans

# statsmodels（统计模型）
from statsmodels.tsa.arima.model import ARIMA

# scipy（科学计算）
from scipy.optimize import linprog
```

**实践任务：**
```
运行并理解项目中的示例：
1. notebooks/examples/ahp_example.py
2. notebooks/examples/topsis_example.py
3. algorithms/evaluation.py

修改参数，观察结果变化
```

---

#### 阶段4：Git协作（赛前1-2周）⭐ 重要

**必须精通：**
```bash
# 每天开始工作前
git pull origin main           # 拉取队友更新

# 完成一部分工作
git add .
git commit -m "完成第一问代码"
git push origin main

# 查看状态
git status
git log
```

**处理冲突：**
```bash
# 如果push时提示冲突
git pull                       # 拉取更新
# 手动编辑冲突文件
git add <冲突文件>
git commit -m "解决冲突"
git push
```

**团队协作演练：**
```
和队友一起：
1. 故意修改同一文件
2. 练习解决冲突
3. 熟悉pull-commit-push流程

重要：提前练习，比赛时不慌
```

---

#### 阶段5：实战准备（赛前1周）

**环境检查：**
```
□ Python环境正常
□ 所有库都能导入
□ VSCode配置完成
□ Git协作熟练
□ 能快速找到参考代码
□ 常用代码片段准备好
```

**代码模板准备：**
```python
# 准备常用代码片段
# 数据读取
df = pd.read_csv('data.csv')

# 数据清洗
df.dropna()
df.fillna(df.mean())

# 标准化
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaled = scaler.fit_transform(data)

# 绘图（300 DPI）
plt.savefig('result.png', dpi=300, bbox_inches='tight')
```

---

### 💡 编程手要点

**你的核心价值：**
```
✅ 快速实现模型
✅ 数据清洗处理
✅ 生成高质量图表
✅ 代码稳定可靠
✅ 结果准确无误
```

**比赛时的工作流：**
```
Day 1: 数据预处理，第一问代码框架
Day 2: 完成前两问代码和图表
Day 3: 完成所有问题，优化图表
Day 4: 补充实验，灵敏度分析
Day 5: 最终检查，确保无误
```

**工作输出：**
```
- 可运行的Python代码
- 处理后的数据（CSV）
- 高质量图表（300 DPI PNG）
- 计算结果
- 代码说明文档
```

---

## ✍️ 写作手学习路线

> 你负责：论文撰写、LaTeX排版、翻译润色、流程图绘制

### 🎯 需要安装的工具

#### 必需工具：
```
✅ Git（已安装）
✅ VSCode（已安装）
❌ Python（不需要！）
✅ LaTeX环境（在线或本地）
```

**⚠️ 重要：写作手不需要安装Python！**

#### LaTeX环境配置：

**✅ 推荐方案：VSCode + LaTeX本地环境 ⭐⭐⭐**

**为什么强烈推荐本地环境？**
```
✅ 功能强大（自动补全、实时预览）
✅ 完全离线，编译速度快
✅ 与Git完美集成，团队协作方便
✅ 完全免费，无任何限制
✅ 一次配置，终身受益
✅ 比赛时更稳定（不依赖网络）
```

**安装步骤（Mac）：**
```bash
# 1. 安装MacTeX（约4GB，需要20-30分钟）
brew install --cask mactex

# 2. 验证安装
pdflatex --version

# 3. 安装VSCode插件
# 打开VSCode → Extensions → 搜索：LaTeX Workshop
```

**安装步骤（Windows）：**
```
1. 下载MiKTeX：https://miktex.org/download
2. 安装（选择"Install missing packages on-the-fly: Yes"）
3. 验证：打开CMD，输入 pdflatex --version
4. VSCode安装LaTeX Workshop插件
```

**详细配置说明：** 见 `templates/07_README.md`

---

**🔄 备选方案：Overleaf在线（不推荐，仅作备份）**

**仅适合以下情况：**
```
⭕ 本地环境配置失败，临时应急
⭕ 作为备份方案（主方案还是用本地）
```

**为什么不推荐 Overleaf？**
```
❌ 免费版有严格限制（编译超时）
❌ 3人协作需要付费升级
❌ 需要稳定网络，断网无法工作
❌ 大项目编译很慢
❌ 比赛时网络不稳定风险高
```

**如果实在需要用：**
```
1. 访问 https://www.overleaf.com
2. 用学校邮箱注册
3. 创建项目，上传模板
4. 建议：仅作为备份，主环境用VSCode本地
```

**⚠️ 重要提醒：强烈建议提前配置好VSCode本地环境，比赛时更稳定！**

#### VSCode插件（写作手）：
```
必装：
1. GitLens（Git可视化）
2. LaTeX Workshop（如果用本地LaTeX）
3. Markdown All in One（写文档）

推荐：
4. Spell Right（拼写检查）
5. Grammarly（语法检查，浏览器插件）
```

---

### 📚 学习路径（写作手）

#### 阶段1：熟悉美赛论文（3-5天）

**必读文档：**
```
1. README.md
2. docs/04_mcm_guide.md（美赛评审机制）⭐
3. templates/07_README.md（LaTeX教程）⭐
4. templates/08_LATEX_CHEATSHEET.md（命令速查）
```

**阅读O奖论文：**
```
打开 past_problems/ 目录
精读2-3篇O奖论文，重点看：

1. 摘要怎么写（最重要！）
2. 引言结构
3. 图表设计（配色、标注）
4. 假设表述
5. 结论写法
```

**理解美赛特点：**
```
✅ 摘要决定命运（占分40%）
✅ 假设要充分
✅ 检验越多越好
✅ 图表要精美
✅ 创新可容错
```

---

#### 阶段2：LaTeX入门（1周）⭐ 核心

**Day 1：看视频教程**
```
B站搜索：「美赛LaTeX教程」或「VSCode LaTeX配置」
推荐关键词：
- VSCode LaTeX Workshop教程
- mcmthesis模板教程
- 美赛论文写作
- LaTeX Workshop使用

看2-3个视频（每个20-30分钟）
```

**Day 2-3：配置VSCode LaTeX环境**
```
1. 安装LaTeX引擎
   Mac: brew install --cask mactex
   Windows: 下载安装 MiKTeX (https://miktex.org)

2. 安装VSCode插件
   打开VSCode → Extensions → 搜索安装：
   ✓ LaTeX Workshop

3. 打开本项目模板
   VSCode → File → Open Folder
   → 打开 templates/latex/mcmthesis/
   → 打开 mcmthesis-demo.tex

4. 编译预览
   → Ctrl+Alt+B (Windows) 或 Cmd+Option+B (Mac)
   → 或点击右上角绿色播放按钮
   → 查看生成的PDF

5. 修改demo文件练习

💡 详细配置见：templates/07_README.md
```

**Day 4-6：练习常用命令**

**必须掌握（打印速查表）：**
```latex
% 1. 插入图片
\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.8\textwidth]{result.png}
    \caption{Results}
    \label{fig:result}
\end{figure}

% 2. 插入表格
\begin{table}[htbp]
    \centering
    \caption{Parameters}
    \begin{tabular}{cc}
        \hline
        Name & Value \\
        \hline
        $\alpha$ & 0.01 \\
        \hline
    \end{tabular}
\end{table}

% 3. 数学公式
行内：$y = mx + c$
独立：
\begin{equation}
    E = mc^2
    \label{eq:mass}
\end{equation}

% 4. 引用
See Figure \ref{fig:result}.
See Equation \ref{eq:mass}.
```

**实践任务：**
```
用LaTeX写一篇简单文档，包含：
- 标题、摘要
- 2-3个章节
- 插入1张图片
- 插入1个表格
- 写2-3个公式
- 添加参考文献

目标：熟悉基本操作，不追求完美
```

**Day 7：团队协作练习（Git）**
```
使用Git进行LaTeX团队协作：
1. 建立Git仓库协作
2. 每人负责不同section文件
3. 练习提交、合并

工作流：
git pull                    # 开始前拉取
# 编辑 sections/model.tex
git add sections/model.tex
git commit -m "完成模型推导"
git push

备选：Overleaf在线协作
- 优点：实时协作
- 缺点：免费版只能邀请1人，3人需升级
```

---

#### 阶段3：英文写作（1周）

**摘要写作（最重要）⭐⭐⭐**

**必须回答4个问题：**
```
1. 问题是什么？（Problem）
2. 我们做了什么？（Approach）
3. 结论是什么？（Results）
4. 建议是什么？（Recommendations）
```

**摘要模板（背下来）：**
```
[Problem]
We address the problem of [具体问题]. 
This is important because [重要性].

[Approach]
To solve this, we develop a [模型] model that [做什么]. 
Specifically, we:
- First, [步骤1]
- Then, [步骤2] using [方法]
- Finally, [步骤3]

[Results]
Our results show that [发现1]. Specifically, [数据]. 
We also find that [发现2], with [量化结果].

[Recommendations]
Based on our analysis, we recommend [建议1] and [建议2].

Keywords: [3-5个关键词]
```

**学习资源：**
```
1. 阅读O奖论文的摘要（past_problems/）
2. 模仿优秀摘要的结构
3. 使用DeepL/ChatGPT辅助翻译
```

**常用学术表达：**
```
开头：
- We address the problem of...
- This paper investigates...
- We develop a model to...

方法：
- To solve this, we...
- We employ/utilize/apply...
- Our approach consists of...

结果：
- Our results show/demonstrate/indicate that...
- We find that...
- The analysis reveals...

结论：
- Based on our analysis, we recommend...
- We conclude that...
- This suggests that...
```

---

#### 阶段4：翻译工具（1-2天）

**必备工具：**

**1. DeepL（推荐）⭐**
```
访问：https://www.deepl.com
或下载客户端

使用技巧：
- 整段翻译，不要逐句
- 翻译后自己润色
- 保持专业术语准确
```

**2. ChatGPT（润色）**
```
提示词：
"请将以下中文翻译成学术英语，用于数学建模论文：
[你的中文]"

或：
"请润色以下学术英语段落：
[你的英文]"
```

**3. Grammarly（语法检查）**
```
安装VSCode插件或浏览器插件
实时检查语法错误
免费版够用
```

**⚠️ 注意：** 翻译工具是辅助，不能完全依赖！

---

#### 阶段5：流程图绘制（2-3天）

**逻辑类图表（写作手负责）：**
```
- 整体流程图
- 模型框架图
- 问题分析图
- 层次结构图
```

**推荐工具：**

**1. Draw.io（免费，推荐）⭐**
```
访问：https://app.diagrams.net
或下载客户端

优点：
- 免费
- 简单易用
- 导出高清PNG
```

**2. ProcessOn（国内）**
```
访问：https://www.processon.com
需要注册
```

**3. PowerPoint**
```
简单快速
直接画图
另存为PNG
```

**实践任务：**
```
画一个简单的流程图：
数据输入 → 预处理 → 建模 → 求解 → 结果分析

要求：
- 清晰明了
- 配色协调
- 导出300 DPI
```

---

#### 阶段6：Git协作（赛前1-2周）

**写作手的Git使用：**

**日常工作流：**
```bash
# 早上开始工作前
cd MathModelHub/competitions/2026/paper
git pull origin main           # 拉取更新

# 写作过程中（随时提交）
git add main.tex
git commit -m "完成引言部分"
git push origin main

# 收到编程手的图表后
git pull                       # 拉取最新图表
# 在LaTeX中插入图片
git add main.tex
git commit -m "添加第一问图表"
git push
```

**⚠️ 重要：** 每次开始工作前先`git pull`！

**避免冲突的技巧：**
```
1. 不同人编辑不同文件
   - 写作手：main.tex
   - 建模手：sections/model.tex
   - 编程手：figures/（图片）

2. 实时沟通
   "我正在改main.tex，你们先别动"

3. 频繁提交
   每完成一小部分就commit
```

---

#### 阶段7：实战准备（赛前1周）

**检查清单：**
```
□ VSCode + LaTeX环境配置完成
□ LaTeX基本操作熟练
□ 摘要写作模板背熟
□ 翻译工具准备好（DeepL、ChatGPT）
□ 流程图工具熟悉
□ Git操作熟练
□ 打印LaTeX速查表
□ 打印摘要模板
□ (可选) Overleaf账号作为备选
```

**准备资料：**
```
□ 收集常用学术表达
□ 准备参考文献格式
□ 阅读3-5篇O奖论文
□ 总结优秀图表设计
□ 准备论文检查清单
```

**模拟练习：**
```
选一道历年题目
用2-3小时：
- 搭建论文框架
- 写引言
- 画流程图
- 写假设

目标：熟悉流程，提高速度
```

---

### 💡 写作手要点

**你的核心价值：**
```
✅ 撰写高质量摘要（决定命运）
✅ 论文结构清晰
✅ 假设表述充分
✅ 英文表达专业
✅ 排版精美
✅ 无语法错误
```

**比赛时的工作流：**
```
Day 1: 
- 搭建论文框架
- 写引言、问题重述
- 画整体流程图

Day 2-3:
- 收到结果立即写对应部分
- 边做边写
- 不要等所有结果出来

Day 4:
- 完成中文稿
- 翻译（DeepL）
- 润色（ChatGPT）
- 美化排版

Day 5:
- 写摘要（最后写）
- 最终检查
- 提交
```

**工作输出：**
```
- 完整的LaTeX源码
- 流程图、框架图
- 翻译后的英文稿
- 最终PDF论文
```

**⚠️ 最重要的事：**
```
摘要！摘要！摘要！
占分40%，决定初评
必须独立完整
不看正文也能理解全文
```

---

## 🤝 团队协作要点（所有人）

### Git协作规范

**每日工作流程：**
```
上午9:00开会（15分钟站会）
├─ 昨天完成了什么
├─ 今天计划做什么
└─ 遇到什么困难

开始工作前：
git pull origin main        # 先拉取

工作过程中：
git add .
git commit -m "完成xx"
git push origin main        # 及时推送

晚上22:00总结：
- 同步进度
- 解决问题
- 明天计划
```

### 分工协作

**避免冲突的文件组织：**
```
competitions/2026/
├── problem_analysis/       # 共同讨论
├── code/                   # 编程手负责
├── data/                   # 编程手负责
├── paper/
│   ├── main.tex           # 写作手负责
│   ├── sections/          
│   │   ├── model.tex      # 建模手撰写
│   │   └── analysis.tex   # 写作手撰写
│   └── figures/           # 编程手提供
└── results/               # 编程手提供
```

### 沟通技巧

**好的沟通：**
```
✅ "第一问LSTM结果出来了，R²=0.92，
    图表在figures/q1_prediction.png"

✅ "我正在改main.tex第3-5节，
    30分钟内不要push修改这部分"

✅ "灵敏度分析需要测试学习率0.001, 0.01, 0.1，
    大概需要2小时"
```

**不好的沟通：**
```
❌ "弄好了"（什么弄好了？）
❌ "有问题"（什么问题？）
❌ "改一下"（改什么？）
```

---

## 📅 完整时间表总结

### 6周完整规划

| 角色 | Week 1-2 | Week 3-4 | Week 5 | Week 6 |
|------|---------|---------|--------|--------|
| **建模手** | Git + 熟悉项目 | 学习算法（AHP等） | Python验证 | 团队磨合 |
| **编程手** | Git + Python基础 | 数据分析（NumPy等） | 算法实现 | 团队磨合 |
| **写作手** | Git + 读O奖论文 | LaTeX学习 | 英文写作 | 团队磨合 |

### 2周冲刺版（最小必学）

| 角色 | Week 1 | Week 2 |
|------|--------|--------|
| **建模手** | Git(2天) + AHP/TOPSIS(5天) | 团队磨合(7天) |
| **编程手** | Git(2天) + Python基础(5天) | 团队磨合(7天) |
| **写作手** | Git(2天) + LaTeX(5天) | 团队磨合(7天) |

---

## 📋 检查清单（按角色）

### 建模手检查清单

**工具环境：**
```
□ Git安装并配置
□ Python环境可用
□ VSCode配置完成
□ 能运行项目示例
```

**技能掌握：**
```
□ Git基础操作
□ AHP/TOPSIS熟练
□ 能用Python验证
□ 阅读过O奖论文
□ 了解假设提出方法
```

**资料准备：**
```
□ 打印算法手册
□ 准备判断矩阵模板
□ 收集常用参数
```

---

### 编程手检查清单

**工具环境：**
```
□ Git安装并配置
□ Python完整环境
□ 所有库能导入
□ VSCode配置完成
□ Git协作熟练
```

**技能掌握：**
```
□ Git基础操作
□ NumPy/Pandas熟练
□ 数据可视化
□ 能找到参考代码
□ 会调试修改代码
```

**资料准备：**
```
□ 常用代码片段
□ 数据处理模板
□ 可视化配色方案
```

---

### 写作手检查清单

**工具环境：**
```
□ Git安装并配置
□ VSCode + LaTeX环境配置完成
□ 翻译工具准备好
□ 流程图工具熟悉
□ (可选) Overleaf账号作为备选
```

**技能掌握：**
```
□ Git基础操作
□ LaTeX基本操作
□ 摘要写作模板背熟
□ 常用学术表达
□ 能画流程图
```

**资料准备：**
```
□ 打印LaTeX速查表
□ 打印摘要模板
□ 收集学术表达
□ 阅读O奖论文
```

---

## 🚀 现在开始行动

### 今天就做（所有人）

```bash
# Step 1: 安装Git
# 参考"通用准备"部分

# Step 2: 注册GitHub
# 访问 https://github.com

# Step 3: 克隆项目
git clone https://github.com/Jaxon1216/MathModelHub.git
cd MathModelHub

# Step 4: 根据你的角色
# 建模手：安装Python，pip install -r requirements.txt
# 编程手：安装Anaconda，pip install -r requirements.txt
# 写作手：配置VSCode + LaTeX环境（见templates/07_README.md）
```

### 本周任务（按角色）

**建模手：**
```
- 熟悉项目结构
- 开始学习Git
- 阅读算法手册
- 运行示例代码
```

**编程手：**
```
- 配置Python环境
- 开始学习Git
- 学习NumPy基础
- 运行示例代码
```

**写作手：**
```
- 配置VSCode + LaTeX环境
- 开始学习Git
- 阅读O奖论文
- 看LaTeX视频教程
```

---

## 💪 记住

**对所有角色：**
- ✅ Git是必学的（团队协作核心）
- ✅ 循序渐进，不要贪多
- ✅ 动手实践比看教程重要
- ✅ 提前1-2周团队磨合

**对建模手：**
- ✅ 重理论，轻编程
- ✅ 精通2-3个高频模型即可
- ✅ Python能验证就行

**对编程手：**
- ✅ 熟练数据处理
- ✅ 能快速找代码改代码
- ✅ Git要非常熟练

**对写作手：**
- ✅ LaTeX是必须的
- ✅ 摘要决定命运
- ✅ 论文完整比完美重要
- ✅ 不需要Python

---

## 📚 相关资源

### 项目内资源
- **通用指南**：README.md, 01_QUICKSTART.md
- **美赛指南**：docs/04_mcm_guide.md
- **团队协作**：docs/05_team_workflow.md（含5天时间轴）
- **算法手册**：docs/06_algorithms_reference.md
- **LaTeX教程**：templates/07_README.md
- **LaTeX速查**：templates/08_LATEX_CHEATSHEET.md

### 外部资源
- **Git教程**：https://notes.jiangxu.net/Misc/tools/git.html
- **Python教程**：B站搜索「Python零基础」
- **LaTeX教程**：B站搜索「美赛LaTeX」或「VSCode LaTeX Workshop」
- **VSCode LaTeX配置**：见 templates/07_README.md
- **Overleaf（备选）**：https://www.overleaf.com

---

## 📞 遇到问题？

- 查看项目docs/目录下的详细文档
- 参考past_problems/历年真题
- 或提Issue到GitHub

**作者联系方式：**
- 邮箱：jiangxu05@outlook.com
- GitHub：[github.com/Jaxon1216](https://github.com/Jaxon1216)

---

**🏆 祝你们学习顺利，美赛取得好成绩！**
