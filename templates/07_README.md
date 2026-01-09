# 美赛论文模板使用指南

> 📺 **强烈建议**：先在B站搜索「**美赛LaTeX教程**」或「**VSCode LaTeX配置**」看10-30分钟视频！
> 
> 推荐关键词：美赛LaTeX模板 | MCM论文写作 | VSCode LaTeX Workshop | mcmthesis使用

---

## 📂 模板文件结构

```
templates/
├── README.md                    # 本文件（一站式教程）
├── LATEX_CHEATSHEET.md          # LaTeX命令速查表
├── latex/mcmthesis/             # LaTeX模板
│   ├── mcmthesis.cls           # ⭐ 核心类文件（必需）
│   ├── mcmthesis-demo.tex      # 示例文件
│   └── mcmthesis-demo.pdf      # 效果预览
└── word/
    └── MCM_Template.docx        # Word模板
```

---

## 🚀 快速开始（5分钟）

### 方式1：VSCode本地（强烈推荐）⭐

**为什么选择VSCode + LaTeX？**
- ✅ 排版专业（O奖论文几乎都用LaTeX）
- ✅ 公式美观、自动编号
- ✅ 功能强大：自动补全、实时预览、错误检查
- ✅ 完全离线，速度快，无限制
- ✅ 集成Git，版本控制方便
- ✅ 完全免费

**3步开始：**

```
Step 1: 安装LaTeX引擎
→ Mac用户：brew install --cask mactex
→ Windows用户：下载安装 MiKTeX (https://miktex.org)
→ 等待安装完成（首次约5GB，需15-30分钟）

Step 2: 安装VSCode插件
→ 打开VSCode
→ 左侧Extensions（或Ctrl/Cmd+Shift+X）
→ 搜索并安装：LaTeX Workshop

Step 3: 打开模板开始写作
→ VSCode → File → Open Folder
→ 打开：templates/latex/mcmthesis/
→ 打开文件：mcmthesis-demo.tex
→ 按 Ctrl+Alt+B (Win) 或 Cmd+Option+B (Mac) 编译
→ 或点击右上角绿色播放按钮
→ 查看生成的PDF，开始写作！
```

**团队协作（Git）：**
```
使用Git进行版本控制和团队协作：
→ 每人负责不同section文件
→ 实时commit和push
→ 完全免费，无人数限制

工作流：
git pull                    # 开始前拉取更新
# 编辑LaTeX文件
git add .
git commit -m "完成引言部分"
git push                    # 推送到远程
```

---

### 方式2：Overleaf在线（不推荐，仅作备份）

**⚠️ 不推荐原因：**
- ❌ 免费版有严格限制（编译超时、项目数量限制）
- ❌ 3人协作需要付费升级
- ❌ 需要稳定网络，比赛时有风险
- ❌ 大项目编译慢
- ❌ 不如VSCode功能强大

**仅适合：**
- ⭕ 本地环境配置失败，临时应急
- ⭕ 作为备份方案（主环境还是用VSCode）

**如果非要使用：**

```
Step 1: 注册Overleaf
→ 访问 https://www.overleaf.com
→ 用学校邮箱注册（教育版额度更高）

Step 2: 创建项目并上传模板
→ New Project → Upload → 上传：
   ✓ latex/mcmthesis/mcmthesis.cls
   ✓ latex/mcmthesis/mcmthesis-demo.tex

Step 3: 开始编辑
→ 参考demo文件写作
```

**❗ 重要提醒：强烈建议使用VSCode本地环境，比赛时更稳定可靠！**

---

### 方式3：Word模板（简单但不推荐）

```
打开：word/MCM_Template.docx
填写摘要页，开始写作

⚠️ 注意：Word排版不如LaTeX专业，O奖论文很少用Word
```

---

## ⚙️ VSCode LaTeX 详细配置（推荐方案）⭐

### 1. 安装LaTeX引擎

#### Mac用户（推荐MacTeX）：
```bash
# 使用Homebrew安装（推荐）
brew install --cask mactex

# 安装后验证
xelatex --version
```

#### Windows用户（推荐MiKTeX）：
```
1. 访问 https://miktex.org/download
2. 下载并安装MiKTeX
3. 安装时选择"Install missing packages automatically"
4. 验证：打开CMD，输入 xelatex --version
```

⏱️ **预计时间：** 15-30分钟（首次约5GB下载）

---

### 2. 安装VSCode插件

```
打开VSCode
→ 点击左侧Extensions图标（或Ctrl/Cmd+Shift+X）
→ 搜索：LaTeX Workshop
→ 点击Install安装（作者：James Yu）

推荐同时安装：
→ Code Spell Checker（拼写检查）
→ Grammarly（语法检查）
```

---

### 3. 配置VSCode（可选，提升体验）

按 `Ctrl/Cmd + ,` 打开设置，搜索"latex"，或直接编辑 `settings.json`：

```json
{
    // 保存时自动编译
    "latex-workshop.latex.autoBuild.run": "onSave",
    
    // 使用xelatex编译（支持中文）
    "latex-workshop.latex.recipes": [
        {
            "name": "xelatex",
            "tools": ["xelatex"]
        }
    ],
    
    "latex-workshop.latex.tools": [
        {
            "name": "xelatex",
            "command": "xelatex",
            "args": [
                "-synctex=1",
                "-interaction=nonstopmode",
                "-file-line-error",
                "%DOC%"
            ]
        }
    ],
    
    // PDF预览设置
    "latex-workshop.view.pdf.viewer": "tab",
    
    // 清理辅助文件
    "latex-workshop.latex.clean.fileTypes": [
        "*.aux", "*.bbl", "*.blg", "*.idx", "*.ind", 
        "*.lof", "*.lot", "*.out", "*.toc", "*.acn", 
        "*.acr", "*.alg", "*.glg", "*.glo", "*.gls", 
        "*.ist", "*.fls", "*.log", "*.fdb_latexmk"
    ]
}
```

---

### 4. 开始使用

```bash
# 打开模板目录
cd templates/latex/mcmthesis
code .

# 在VSCode中打开 mcmthesis-demo.tex
# 编译方式1：Ctrl/Cmd + Alt + B
# 编译方式2：点击右上角绿色播放按钮
# 编译方式3：保存文件自动编译（如果启用了autoBuild）

# 查看PDF：编译后会自动打开预览
```

**快捷键：**
```
Ctrl/Cmd + Alt + B    # 编译
Ctrl/Cmd + Alt + V    # 查看PDF
Ctrl/Cmd + Alt + J    # 跳转到PDF对应位置
Ctrl/Cmd + Alt + C    # 清理辅助文件
```

---

### 5. Git团队协作

**推荐工作流：**

```bash
# 每天开始工作前
git pull origin main

# 编辑LaTeX文件
# VSCode会自动编译并预览

# 完成一部分后提交
git add .
git commit -m "完成引言和问题重述"
git push origin main
```

**避免冲突的文件组织：**
```
paper/
├── main.tex                # 主文件（写作手负责）
├── sections/
│   ├── introduction.tex    # 引言（写作手）
│   ├── model.tex          # 模型推导（建模手）
│   ├── analysis.tex       # 结果分析（写作手）
│   └── conclusion.tex     # 结论（写作手）
└── figures/               # 图片（编程手提供）
```

---

### 6. 常见问题

**Q1: 编译失败，显示"xelatex not found"**
```
A: LaTeX引擎未安装或未添加到PATH
   Mac: brew install --cask mactex
   Windows: 重新安装MiKTeX并勾选"Add to PATH"
```

**Q2: 中文显示乱码**
```
A: 使用xelatex编译（不要用pdflatex）
   VSCode会自动选择xelatex
```

**Q3: 编译慢**
```
A: 首次编译较慢（安装宏包），后续会快很多
   可以注释掉暂时不用的章节加速编译
```

**Q4: PDF不更新**
```
A: 清理辅助文件再编译
   Ctrl/Cmd + Alt + C，然后重新编译
```

---

## 📖 LaTeX基础（够用版）

### mcmthesis模板基本结构

```latex
\documentclass{mcmthesis}

% 设置队伍信息
\mcmsetup{
    CornNumber = 2312345,        % 控制号
    Problem = C,                 % 题目
    Year = 2026,
    Title = Your Paper Title,
}

\begin{document}

% 1. 摘要（最重要！）
\begin{abstract}
摘要内容...必须回答4个问题：
- 问题是什么？
- 我们做了什么？
- 结论是什么？
- 建议是什么？
\end{abstract}

\begin{keywords}
Keyword1; Keyword2; Keyword3
\end{keywords}

% 2. 目录
\tableofcontents
\newpage

% 3. 正文
\section{Introduction}
...

\section{Problem Analysis}
...

\section{Model Development}
...

\section{Results}
...

\section{Conclusions}
...

% 4. 参考文献
\bibliographystyle{plain}
\bibliography{references}

\end{document}
```

### 常用命令速查

**插入图片：**
```latex
\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.8\textwidth]{figures/result.png}
    \caption{Prediction Results}
    \label{fig:result}
\end{figure}

引用：See Figure \ref{fig:result}.
```

**插入表格：**
```latex
\begin{table}[htbp]
    \centering
    \caption{Model Parameters}
    \begin{tabular}{ccc}
        \hline
        Parameter & Value & Description \\
        \hline
        $\alpha$ & 0.05 & Learning rate \\
        \hline
    \end{tabular}
\end{table}
```

**数学公式：**
```latex
% 行内公式
Learning rate $\alpha = 0.01$

% 独立公式
\begin{equation}
    y = \beta_0 + \beta_1 x + \epsilon
    \label{eq:linear}
\end{equation}

% 多行公式
\begin{align}
    x &= a + b \\
    y &= c + d
\end{align}
```

**📋 更多命令**：查看 [`LATEX_CHEATSHEET.md`](./LATEX_CHEATSHEET.md)

---

## 📝 论文结构建议

### 1. Summary（摘要）- 最重要！⭐

**必须回答4个问题：**
1. ✅ **问题是什么？**（Problem）
2. ✅ **我们做了什么？**（Approach/Model）  
3. ✅ **结论是什么？**（Results - 要有数据）
4. ✅ **建议是什么？**（Recommendations）

**长度**：1页以内  
**评分占比**：~40%  
**写作要求**：独立完整，不看正文也能理解

**模板：**
```
[Problem]
We address the problem of [具体问题]. This is important because [重要性].

[Approach]
To solve this, we develop a [模型] model that [做什么]. 
Specifically, we:
- First, [步骤1]
- Then, [步骤2] using [方法]
- Finally, [步骤3]

[Results]
Our results show that [发现1]. Specifically, [具体数据]. 
We also find that [发现2], with [量化结果].

[Recommendations]
Based on our analysis, we recommend [建议1] and [建议2].

Keywords: [3-5个关键词]
```

### 2. Introduction（引言）
- 问题背景
- 文献综述
- 论文组织结构

### 3. Problem Analysis（问题分析）
- 问题分解
- 关键因素识别
- 建模思路流程图

### 4. Assumptions（假设）⭐ 重要
- 列出所有假设
- 说明合理性
- 分析影响

### 5. Model Development（模型建立）
- 符号说明
- 模型推导
- 算法流程

### 6. Model Solution（模型求解）
- 数据处理
- 参数确定
- 求解过程

### 7. Model Analysis（模型分析）⭐ 重要
- 灵敏度分析
- 稳定性分析
- 误差分析

### 8. Results（结果）
- 数据可视化
- 结果解释

### 9. Conclusions（结论）
- 模型优缺点
- 改进方向
- 政策建议

### 10. References（参考文献）

---

## 💡 美赛写作要点

### 关键特点

1. **摘要决定命运**  
   初评主要看摘要，写不好论文再好也难获奖

2. **假设要充分**  
   美赛极度重视假设的合理性和必要性

3. **检验越多越好**  
   灵敏度分析、稳定性分析、误差分析

4. **图表要精美**  
   高分辨率（300 DPI）、配色协调、标注清晰

5. **创新可容错**  
   有创新即使有小错误也可能获奖

### 常见错误 ❌

- 摘要太简单或太差
- 假设不够充分
- 没有模型检验
- 图表质量差（模糊、低分辨率）
- 论文不完整
- 语法错误多

### 正确做法 ✅

- 摘要反复修改，独立完整
- 详细说明所有假设
- 多做灵敏度分析
- 图表300 DPI，专业配色
- 确保每个问题都有结论
- 使用Grammarly检查语法

---

## ⚠️ 常见问题

### LaTeX编译问题

**Q: "mcmthesis.cls not found"**
```
A: mcmthesis.cls必须和.tex文件在同一目录
   VSCode: 放在同一文件夹
   Overleaf: 上传到项目根目录
```

**Q: 中文显示乱码**
```
A: 使用XeLaTeX编译，不要用PDFLaTeX
```

**Q: 图片无法显示**
```
A: 检查路径是否正确
   推荐：\includegraphics{figures/result.png}
```

**Q: 参考文献格式错误**
```
A: 完整编译流程：
   xelatex main.tex
   bibtex main
   xelatex main.tex
   xelatex main.tex
```

### Overleaf问题（如果使用在线方案）

**Q: 编译超时**
```
A: 免费版有限制
   推荐：改用VSCode本地编译（无限制）
   备选：
   - 压缩图片
   - 升级付费版
```

**Q: 无法上传大文件**
```
A: 免费版限制<50MB
   推荐：改用VSCode本地编译（无限制）
   备选：
   - 压缩图片
   - 使用外部图床
```

**Q: 3人协作怎么办？**
```
A: 免费版只能邀请1人
   推荐：使用VSCode+Git协作（无人数限制）⭐
   备选：
   - 用教育邮箱申请免费升级
   - 或升级付费版（$15/月）
```

### Word问题

**Q: 公式编号不连续**
```
A: 使用「插入题注」，不要手动编号
```

**Q: 图片位置乱跑**
```
A: 右键图片 → 自动换行 → 嵌入型
```

---

## 🎓 学习路径

### 赛前1周（推荐）

```
Day 1-2: 看B站视频（1-2小时）
         配置VSCode + LaTeX环境，试用模板

Day 3-4: 练习写一篇简单文档
         学习插入图表、公式

Day 5-7: 和队友测试协作
         准备常用代码片段
```

### 比赛时（5天）

```
Day 1: 搭建框架，写引言
Day 2-3: 边做边写，及时更新
Day 4: 翻译、排版、美化图表
Day 5: 写摘要、最终检查
```

---

## 📋 提交前检查清单

```
□ 控制号（Control Number）填写正确
□ 题目选择（Problem Chosen）正确
□ 摘要完整（问题-方法-结果-建议）
□ 所有图表清晰（300 DPI）
□ 所有公式有编号并被引用
□ 参考文献格式统一
□ 无明显语法错误（Grammarly检查）
□ 页数 ≤ 25页
□ PDF文件名符合要求
```

---

## 📚 相关资源

### 项目内资源
- **LaTeX命令速查**：[`LATEX_CHEATSHEET.md`](./LATEX_CHEATSHEET.md)
- **论文写作指南**：[`../docs/04_mcm_guide.md`](../docs/04_mcm_guide.md)
- **团队协作流程**：[`../docs/05_team_workflow.md`](../docs/05_team_workflow.md)
- **算法使用手册**：[`../docs/06_algorithms_reference.md`](../docs/06_algorithms_reference.md)

### 在线教程
- **LaTeX Workshop文档**：https://github.com/James-Yu/LaTeX-Workshop/wiki
- **Overleaf文档（备用）**：https://www.overleaf.com/learn
- **LaTeX符号查询**：http://detexify.kirelabs.org/classify.html
- **表格生成器**：https://www.tablesgenerator.com/
- **B站搜索**：美赛LaTeX教程

---

**💡 温馨提示**：LaTeX学习曲线陡峭，建议提前1-2周开始学习，不要临时抱佛脚！

**🎓 祝论文写作顺利，美赛取得好成绩！**
