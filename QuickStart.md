# 🚀 快速开始指南

## 环境配置

### 1. 安装依赖

```bash
cd MathModelHub
pip install -r requirements.txt
```

或者安装为Python包：

```bash
pip install -e .
```

### 2. 验证安装

```bash
python -c "import numpy, pandas, matplotlib, sklearn; print('环境配置成功！')"
```

## 📚 快速使用

### 使用Jupyter Notebook可视化

本项目提供预制的可视化Notebook，可直接运行：

```bash
# 启动Jupyter
jupyter notebook

# 打开 data_analysis/visualization/ 目录下的notebook
# 例如：01_直方图_分布分析.ipynb
```

**可用的可视化Notebook：**
- `01_直方图_分布分析.ipynb` - 数据分布分析
- `02_箱线图_异常值检测.ipynb` - 异常值检测
- `03_折线图_趋势分析.ipynb` - 时间序列趋势
- `04_热力图_相关性矩阵.ipynb` - 相关性分析
- `05_柱状图_分组对比.ipynb` - 分组对比
- `06_散点图_预测评估.ipynb` - 预测效果评估

### 使用论文模板

**快速开始：查看 [`templates/07_README.md`](./templates/07_README.md)**

#### LaTeX + VSCode（强烈推荐）⭐⭐⭐

**Mac安装：**
```bash
# 1. 安装LaTeX（约4GB，需20-30分钟）
brew install --cask mactex

# 2. VSCode安装插件：LaTeX Workshop
```

**Windows安装：**
```
1. 下载 MiKTeX: https://miktex.org/download
2. 安装（选择"Install missing packages on-the-fly: Yes"）
3. VSCode安装插件：LaTeX Workshop
```

**使用：**
```
1. 打开 templates/latex/mcmthesis/mcmthesis-demo.tex
2. Ctrl/Cmd + Alt + B: 编译
3. Ctrl/Cmd + Alt + V: 预览PDF
```

**备选：** Overleaf在线（https://www.overleaf.com）

#### Word模板

```
打开 templates/word/MCM_Template.docx
填写摘要页，开始写作
```

**详细教程**：`templates/07_README.md`（含完整配置、使用技巧、常见问题等）  
**命令速查**：`templates/08_LATEX_CHEATSHEET.md`

### 查看完整建模案例

`data_analysis/preprocessing/2025C示例/` 目录包含完整的美赛C题建模分析案例：

```
2025C示例/
├── problem.md              # 题目说明
├── 数据预处理.ipynb         # 数据清洗和处理
├── 模型分析/
│   └── 建模分析.ipynb      # 完整建模过程
└── *.csv                   # 原始数据和处理结果
```

## 🎯 参加美赛准备

### 赛前准备清单

- [ ] 熟悉常用算法（见 `algorithms/algorithms_reference.md`）
- [ ] 运行可视化Notebook，熟悉图表制作
- [ ] 测试LaTeX环境（准备好论文模板）
- [ ] 阅读O奖论文（`past_problems/` 目录）
- [ ] 准备翻译工具（DeepL、ChatGPT等）

### 比赛时工作流程

1. **Day 1上午**：选题
   - 在 `competitions/2026/problem_analysis/` 中记录分析
   
2. **Day 1下午-Day 3**：建模求解
   - 代码存放在 `competitions/2026/code/`
   - 数据存放在 `competitions/2026/data/`
   
3. **Day 2-Day 4**：论文撰写
   - 使用 `templates/` 中的模板
   - 论文存放在 `competitions/2026/paper/`
   
4. **Day 5上午**：最终检查提交

## 📖 学习路径

### 新手入门（赛前1个月）

1. **第1周**：学习Python基础和NumPy、Pandas
2. **第2周**：掌握评价模型（AHP、熵权法、TOPSIS）
3. **第3周**：学习预测模型（ARIMA、回归分析）
4. **第4周**：练习论文写作，阅读O奖论文

### 快速提升（赛前1周）

1. 运行 `data_analysis/visualization/` 中的所有Notebook
2. 学习 `data_analysis/preprocessing/2025C示例/` 的建模流程
3. 阅读 `docs/mcm_guide.md` 完整指南
4. 熟悉 `algorithms/algorithms_reference.md` 算法手册

## 💡 常用资源快速链接

| 资源 | 位置 | 说明 |
|------|------|------|
| 完整指南 | `docs/mcm_guide.md` | 评审机制、选题策略等 |
| **团队协作** | **`docs/team_workflow.md`** | **详细分工、工具配置、协作流程** ⭐ |
| 算法手册 | `algorithms/algorithms_reference.md` | 算法使用参考 |
| 历年真题 | `past_problems/README.md` | 论文和统计 |
| 论文模板 | `templates/` | LaTeX和Word模板 |
| 可视化示例 | `data_analysis/visualization/` | Jupyter Notebook |

## 🔧 常见问题

### Q: 如何测试环境？

```bash
# 进入项目目录
cd MathModelHub

# 测试核心库
python -c "
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
print('所有核心库导入成功！')
"
```

### Q: 如何运行可视化示例？

```bash
# 启动Jupyter
jupyter notebook

# 在浏览器中打开 data_analysis/visualization/ 目录
# 选择任意 .ipynb 文件运行
```

### Q: 如何准备数据集？

将数据放入 `competitions/2026/data/` 目录，参考 `data_analysis/preprocessing/` 中的预处理Notebook。

## 🎓 学习建议

1. **不要贪多**：重点掌握5-6个高频算法
2. **多跑Notebook**：在 `data_analysis/` 中练习数据分析
3. **看O奖论文**：学习摘要写法和图表设计
4. **练习英文**：提前准备常用表达和模板句
5. **团队协作**：提前分工，明确各自任务

## 📞 获取帮助

- 查看文档：`docs/` 目录
- 运行示例：`data_analysis/` 目录
- 参考历年题：`past_problems/` 目录

---

**祝比赛顺利，取得好成绩！🏆**
