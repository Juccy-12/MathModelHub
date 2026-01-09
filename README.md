# MathModelHub - 美赛数学建模资源库

> 专为美国大学生数学建模竞赛（MCM/ICM）准备的算法模型库、数据分析工具和参赛资源集合

## 📁 目录结构

```
MathModelHub/
├── algorithms/                    # 算法模型核心库
│   ├── optimization/             # 优化算法（线性规划、遗传算法、模拟退火等）
│   ├── statistics/               # 统计模型（回归、时间序列、ARIMA等）
│   ├── machine_learning/         # 机器学习（聚类、预测、随机森林等）
│   ├── graph_theory/             # 图论算法（最短路径、网络流等）
│   ├── simulation/               # 仿真模拟（蒙特卡洛等）
│   └── differential_equations/   # 微分方程求解
│
├── data_analysis/                # 数据分析工具集
│   ├── preprocessing/            # 数据预处理与清洗
│   ├── visualization/            # 可视化工具
│   └── utils/                    # 通用工具函数
│
├── templates/                    # 论文模板
│   ├── latex/mcmthesis/          # LaTeX模板（mcmthesis文档类）
│   ├── word/                     # Word模板（含摘要页）
│   ├── 07_README.md              # 一站式教程（含快速开始）⭐
│   └── 08_LATEX_CHEATSHEET.md    # LaTeX命令速查表
│
├── past_problems/                # 历年真题及优秀论文
│   ├── 2024/
│   ├── 2023/
│   └── README.md                 # 题目索引与分析
│
├── competitions/                 # 比赛工作区
│   └── [按年份组织实际比赛代码、数据、论文]
│
├── datasets/                     # 常用数据集
│   └── [经济、地理、社会等数据]
│
├── references/                   # 参考资料库
│   ├── papers/                   # 学术论文
│   └── tutorials/                # 教程文档
│
├── notebooks/                    # Jupyter实验笔记
│   ├── examples/                 # 算法示例
│   └── tutorials/                # 学习教程
│
└── docs/                         # 项目文档
    ├── 04_mcm_guide.md           # 美赛完整指南
    ├── 05_team_workflow.md       # 团队协作指南（详细分工）
    └── 06_algorithms_reference.md # 算法使用手册
```

## 🎯 美赛快速指南

### 一、赛题类型（MCM/ICM）

| 题目 | 类型 | 特点 | 常用模型 |
|------|------|------|----------|
| **A题** | 连续型 | 微分方程、物理机理 | 微分方程、物理建模 |
| **B题** | 离散型 | 图论、组合优化 | 图论算法、启发式算法 |
| **C题** | 大数据 | 数据分析、预测 | 时间序列、机器学习 |
| **D题** | 运筹学 | 网络优化、规划 | 线性规划、网络流 |
| **E题** | 可持续性 | 评价决策 | AHP、熵权法、TOPSIS |
| **F题** | 政策 | 开放问题、政策制定 | 综合评价、回归分析 |

**选题建议**：C/E/F题选择率最高（约70%），相对友好；A/B题需要较强数学基础；D题概念多，慎选。

### 二、评审机制与关键要素

#### 评审三阶段
1. **浏览阶段**（初评）：主要看**摘要质量**和**内容组织**（7分制）
2. **评分阶段**（终评）：详细评分（百分制）
3. **评定阶段**：讨论决定特等奖

#### 摘要写作核心
摘要应回答四个问题：
- ✅ 问题是什么？
- ✅ 我们做了什么？（模型方法）
- ✅ 结论是什么？（重要结果）
- ✅ 建议是什么？（针对问题的直接建议）

#### 美赛与国赛的区别
| 评审维度 | 国赛 | 美赛 |
|---------|------|------|
| **假设合理性** | 一般重视 | **极度重视**，需灵敏度分析 |
| **文字清晰度** | 重视 | **非常重视**，写作能力是核心目标 |
| **建模创造性** | 重视 | **创新可容错**（创新论文即使有错也可获奖）|
| **结果正确性** | 强调 | 相对灵活 |
| **模型检验** | 一般 | **越多越好**，问题分析、结果分析是重点 |

### 三、高频算法模型（O奖论文统计）

#### 评价决策类
- **AHP**（层次分析法）- 出现率最高
- **熵权法（EWM）**
- **TOPSIS法**
- **模糊综合评价**

#### 预测类
- **ARIMA时间序列** - 出现率极高
- **LSTM/神经网络**
- **随机森林**
- **灰色预测GM(1,1)**

#### 优化规划类
- **线性/非线性规划**
- **遗传算法**
- **模拟退火**
- **多目标规划（NSGA-II）**

#### 机器学习类
- **K-means聚类**
- **随机森林**
- **主成分分析（PCA）**
- **回归分析**

#### 其他常见模型
- 蒙特卡洛模拟
- 马尔可夫模型
- 微分方程（ODE/PDE）
- 图论算法（Dijkstra、网络流）

### 四、比赛时间安排（5天）

#### Day 1（选题日）⏰
- **7:00-9:30** 各自读题，记录思路
- **9:30-10:00** 粗筛，排除无思路题目
- **10:00-12:00** 精筛，查资料确定最终选题
- **14:00-18:00** 确定建模方案、论文大纲、数据来源
- **18:00-22:00** 建模手完成第一问，论文手写引言、画流程图

#### Day 2（攻坚日）💪
- 建模手：完成前三问建模
- 编程手：至少完成前两问求解
- 论文手：撰写前两问，参考O奖论文行文逻辑

#### Day 3（冲刺日）🚀
- 完成所有问题建模和求解
- 前三问中文稿必须完成
- 建模/编程手可考虑熬夜

#### Day 4（打磨日）✨
- **上午**：完成整体论文中文稿
- **下午-深夜**：翻译、排版、润色、补充精美插图
- 论文手可熬夜打磨

#### Day 5（提交日）✅
- **8:00-10:00** 三人交叉检查，确认无误后提交

### 五、应急策略

**如果做不出来怎么办？**

> ⚠️ 记住：**完整的论文比什么都重要！**

美赛特点：论文完整 + 排版美观 + 摘要优秀 = 即使结果有问题也有机会获奖

应急措施：
1. 该简化的模型就简化
2. 卡住的地方写进"模型假设"
3. 数据和结果保证能跑通
4. 确保论文完整性和逻辑自洽

## 🚀 快速开始

> 🆕 **完全新手？** 查看 **[新手完整路线图](./02_02_BEGINNER_ROADMAP.md)** 获取从零开始的学习路径！

### 环境配置

```bash
# 克隆项目
git clone https://github.com/Jaxon1216/MathModelHub.git
cd MathModelHub

# 安装依赖
pip install -r requirements.txt

# 或使用国内镜像（更快）
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# 启动Jupyter
jupyter notebook
```

### 使用算法库

```python
# 示例：使用层次分析法
from algorithms.evaluation import AHP

# 示例：时间序列预测
from algorithms.statistics import ARIMAModel

# 示例：数据可视化
from data_analysis.visualization import plot_heatmap
```

## 📖 文档导航与阅读顺序

### 👉 我应该先看哪个文件？

**完全新手（从零开始）：**
```
README.md（你在这里）
  ↓
01_QUICKSTART.md（5分钟快速了解）
  ↓
02_BEGINNER_ROADMAP.md（找到你的角色，按路线学习）⭐⭐⭐
```

**有基础的参赛者：**
```
README.md
  ↓
02_BEGINNER_ROADMAP.md（检查缺漏，按角色补充）
  ↓
docs/04_mcm_guide.md + docs/05_team_workflow.md（深入了解）
```

**只想用模板：**
```
README.md
  ↓
templates/07_README.md（LaTeX/Word模板完整教程）
```

---

### 📚 按编号阅读（推荐顺序）

**入门必读：**
- **[01 快速开始指南](./01_QUICKSTART.md)** - 5分钟快速上手⭐
- **[02 新手完整路线图](./02_BEGINNER_ROADMAP.md)** - 按角色定制的学习路径（核心文档）⭐⭐⭐
- **[03 学习路线总结](./03_ROADMAP_SUMMARY.md)** - 快速查看学习计划

**进阶阅读：**
- **[04 美赛完整指南](./docs/04_mcm_guide.md)** - 评审机制、选题策略、论文写作
- **[05 团队协作指南](./docs/05_team_workflow.md)** - 详细分工、工具配置、协作流程（含5天时间轴）
- **[06 算法使用手册](./docs/06_algorithms_reference.md)** - 美赛高频算法详解

**模板相关：**
- **[07 论文模板教程](./templates/07_README.md)** - LaTeX/Word完整教程⭐
- **[08 LaTeX速查表](./templates/08_LATEX_CHEATSHEET.md)** - 常用命令快速查询

**参考文档：**
- **[09 项目总结](./09_PROJECT_SUMMARY.md)** - 项目创建说明
- **[10 角色对比总结](./10_ROLE_BASED_SUMMARY.md)** - 三个角色详细对比
- **[11 更新日志](./11_UPDATES.md)** - 项目更新记录

---

### 📦 其他资源
- **[历年真题分析](./past_problems/README.md)** - 2016-2024题目统计
- **[数据集说明](./datasets/README.md)** - 常用数据来源
- **[参考资料库](./references/README.md)** - 论文、教程、书籍推荐
- **[Jupyter示例](./notebooks/README.md)** - 算法实例和教程
- **[比赛工作区](./competitions/README.md)** - 比赛期间文件组织

## 📚 外部资源

- [MCM/ICM官网](http://www.comap.com/undergraduate/contests/mcm) - 官方网站
- [COMAP历年题目](https://www.comap.com/undergraduate/contests/mcm/previous-contests.php) - 历年真题
- [O奖论文集](./past_problems/) - 本地优秀论文库

## 🤝 贡献指南

欢迎提交：
- 新的算法实现
- 优化现有代码
- 补充历年真题和解析
- 分享获奖经验

## 📄 许可证

MIT License

---

**💡 提示**：建议在比赛前熟悉本项目的算法库，准备好常用模板和可视化代码，比赛时可直接调用节省时间！

**🎓 祝所有参赛队伍都能取得好成绩！**

## 关于作者
- **邮箱**: jiangxu05@outlook.com
- **GitHub**: [github.com/Jaxon1216](https://github.com/Jaxon1216)
- **博客**: [Jaxon's blog](https://www.jiangxu.net)
- **知识库**: [Jaxon's notes](https://notes.jiangxu.net)