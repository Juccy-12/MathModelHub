# LaTeX 常用命令速查表

> 🎯 快速查找美赛论文写作中最常用的LaTeX命令

## 📖 目录

- [文档结构](#文档结构)
- [文字格式](#文字格式)
- [数学公式](#数学公式)
- [图片插入](#图片插入)
- [表格制作](#表格制作)
- [列表](#列表)
- [引用与标签](#引用与标签)
- [代码块](#代码块)

---

## 文档结构

```latex
% 章节标题
\section{Introduction}           % 一级标题
\subsection{Background}           % 二级标题
\subsubsection{Details}          % 三级标题

% 换页
\newpage

% 目录
\tableofcontents

% 摘要
\begin{abstract}
摘要内容...
\end{abstract}

% 关键词
\begin{keywords}
Keyword1; Keyword2; Keyword3
\end{keywords}
```

---

## 文字格式

```latex
% 加粗
\textbf{bold text}

% 斜体
\textit{italic text}

% 下划线
\underline{underlined text}

% 换行
line 1 \\
line 2

% 新段落（空一行）
Paragraph 1

Paragraph 2

% 引用
``quoted text''  % 正确的引号

% 脚注
This is a text\footnote{This is a footnote}.
```

---

## 数学公式

### 行内公式

```latex
The variable is $x = 5$.
Learning rate $\alpha = 0.01$.
```

### 独立公式（带编号）

```latex
\begin{equation}
    y = \beta_0 + \beta_1 x + \epsilon
    \label{eq:linear}
\end{equation}

% 引用公式
See Equation \ref{eq:linear}.
```

### 独立公式（不带编号）

```latex
\[ y = mx + c \]

% 或
\begin{equation*}
    y = mx + c
\end{equation*}
```

### 多行公式

```latex
% 对齐
\begin{align}
    x &= a + b \\
    y &= c + d \\
    z &= e + f
    \label{eq:system}
\end{align}

% 无编号对齐
\begin{align*}
    x &= a + b \\
    y &= c + d
\end{align*}

% 多行但只有一个编号
\begin{equation}
\begin{split}
    x &= a + b \\
    &= c + d
\end{split}
\end{equation}
```

### 常用数学符号

```latex
% 希腊字母
\alpha, \beta, \gamma, \delta, \epsilon
\theta, \lambda, \mu, \pi, \sigma
\Gamma, \Delta, \Theta, \Lambda, \Sigma

% 上下标
x^2           % x的平方
x_i           % x下标i
x^{2n}        % x的2n次方
x_{i,j}       % x下标i,j

% 分数
\frac{a}{b}   % a/b

% 根号
\sqrt{x}      % 根号x
\sqrt[n]{x}   % n次根号x

% 求和、积分
\sum_{i=1}^{n} x_i           % 求和
\int_{a}^{b} f(x) dx         % 积分
\prod_{i=1}^{n} x_i          % 连乘

% 极限
\lim_{x \to \infty} f(x)

% 偏导数
\frac{\partial f}{\partial x}

% 矩阵
\begin{bmatrix}
    a & b \\
    c & d
\end{bmatrix}

% 向量
\vec{v}       % 向量v
\mathbf{v}    % 粗体向量

% 常用符号
\leq          % ≤
\geq          % ≥
\neq          % ≠
\approx       % ≈
\times        % ×
\cdot         % ·
\in           % ∈
\subseteq     % ⊆
\cup          % ∪
\cap          % ∩
\infty        % ∞
```

---

## 图片插入

### 单张图片

```latex
\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.8\textwidth]{figures/result.png}
    \caption{Prediction Results}
    \label{fig:result}
\end{figure}

% 引用图片
As shown in Figure \ref{fig:result}, ...
```

### 并排图片

```latex
\begin{figure}[htbp]
    \centering
    \begin{minipage}{0.45\textwidth}
        \centering
        \includegraphics[width=\textwidth]{fig1.png}
        \caption{Figure 1}
        \label{fig:1}
    \end{minipage}
    \hfill
    \begin{minipage}{0.45\textwidth}
        \centering
        \includegraphics[width=\textwidth]{fig2.png}
        \caption{Figure 2}
        \label{fig:2}
    \end{minipage}
\end{figure}
```

### 子图（需要subcaption包）

```latex
\usepackage{subcaption}

\begin{figure}[htbp]
    \centering
    \begin{subfigure}{0.45\textwidth}
        \includegraphics[width=\textwidth]{fig1.png}
        \caption{Subfigure 1}
        \label{fig:sub1}
    \end{subfigure}
    \hfill
    \begin{subfigure}{0.45\textwidth}
        \includegraphics[width=\textwidth]{fig2.png}
        \caption{Subfigure 2}
        \label{fig:sub2}
    \end{subfigure}
    \caption{Overall caption}
    \label{fig:overall}
\end{figure}
```

### 图片位置参数

```latex
[htbp]
% h - here (当前位置)
% t - top (页面顶部)
% b - bottom (页面底部)
% p - page (单独一页)
% ! - 强制
```

---

## 表格制作

### 基本表格

```latex
\begin{table}[htbp]
    \centering
    \caption{Model Parameters}
    \label{tab:params}
    \begin{tabular}{ccc}
        \hline
        Parameter & Value & Description \\
        \hline
        $\alpha$ & 0.05 & Learning rate \\
        $\beta$ & 0.9 & Momentum \\
        $n$ & 100 & Iterations \\
        \hline
    \end{tabular}
\end{table}

% 引用表格
See Table \ref{tab:params} for details.
```

### 列对齐方式

```latex
\begin{tabular}{lcr}
% l - 左对齐 (left)
% c - 居中 (center)
% r - 右对齐 (right)
% | - 竖线
```

### 复杂表格

```latex
\begin{table}[htbp]
    \centering
    \caption{Results Comparison}
    \begin{tabular}{|l|c|c|c|}
        \hline
        \textbf{Model} & \textbf{Accuracy} & \textbf{Time} & \textbf{RMSE} \\
        \hline
        LSTM & 0.92 & 45s & 0.08 \\
        ARIMA & 0.85 & 12s & 0.15 \\
        RF & 0.88 & 30s & 0.12 \\
        \hline
    \end{tabular}
\end{table}
```

### 合并单元格

```latex
% 需要 multirow 包
\usepackage{multirow}

\begin{tabular}{|c|c|c|}
    \hline
    \multicolumn{2}{|c|}{Merged} & C \\  % 横向合并
    \hline
    \multirow{2}{*}{Merged} & B & C \\  % 纵向合并
                            & B & C \\
    \hline
\end{tabular}
```

---

## 列表

### 无序列表

```latex
\begin{itemize}
    \item First item
    \item Second item
    \item Third item
        \begin{itemize}
            \item Sub-item 1
            \item Sub-item 2
        \end{itemize}
\end{itemize}
```

### 有序列表

```latex
\begin{enumerate}
    \item First step
    \item Second step
    \item Third step
        \begin{enumerate}
            \item Sub-step 1
            \item Sub-step 2
        \end{enumerate}
\end{enumerate}
```

### 描述列表

```latex
\begin{description}
    \item[Term 1] Description of term 1
    \item[Term 2] Description of term 2
\end{description}
```

---

## 引用与标签

```latex
% 添加标签
\section{Introduction}
\label{sec:intro}

\begin{equation}
    y = mx + c
    \label{eq:line}
\end{equation}

\begin{figure}[htbp]
    ...
    \label{fig:result}
\end{figure}

\begin{table}[htbp]
    ...
    \label{tab:data}
\end{table}

% 引用
See Section \ref{sec:intro}.
See Equation \ref{eq:line}.
See Figure \ref{fig:result}.
See Table \ref{tab:data}.

% 页码引用
See page \pageref{sec:intro}.
```

---

## 代码块

```latex
% 需要 listings 包
\usepackage{listings}
\usepackage{xcolor}

% 配置代码样式
\lstset{
    language=Python,
    basicstyle=\ttfamily\small,
    keywordstyle=\color{blue},
    commentstyle=\color{green},
    stringstyle=\color{red},
    numbers=left,
    numberstyle=\tiny,
    frame=single,
    breaklines=true
}

% 插入代码
\begin{lstlisting}
import numpy as np
import pandas as pd

data = pd.read_csv('data.csv')
print(data.head())
\end{lstlisting}

% 从文件导入代码
\lstinputlisting[language=Python]{code/main.py}
```

---

## 参考文献

### BibTeX格式

```latex
% 在文档末尾
\bibliographystyle{plain}  % 或 ieeetr, apalike等
\bibliography{references}   % references.bib文件

% 在正文中引用
According to \cite{smith2020}, ...
Multiple citations \cite{smith2020,jones2021}.
```

### references.bib示例

```bibtex
@article{smith2020,
    author = {Smith, John and Doe, Jane},
    title = {Deep Learning for Time Series},
    journal = {Journal of ML},
    year = {2020},
    volume = {10},
    pages = {123-145}
}

@book{jones2021,
    author = {Jones, Bob},
    title = {Mathematical Modeling},
    publisher = {Academic Press},
    year = {2021}
}
```

---

## 常用技巧

### 控制页面布局

```latex
% 页边距
\usepackage{geometry}
\geometry{
    a4paper,
    left=2.5cm,
    right=2.5cm,
    top=2.5cm,
    bottom=2.5cm
}

% 行距
\usepackage{setspace}
\onehalfspacing  % 1.5倍行距
\doublespacing   % 2倍行距
```

### 特殊字符

```latex
\%    % 百分号
\$    % 美元符号
\&    % &符号
\_    % 下划线
\#    % 井号
\{    % 左花括号
\}    % 右花括号
~     % 不换行空格
```

### 空格控制

```latex
a\ b        % 普通空格
a~b         % 不换行空格
a\quad b    % 1em空格
a\qquad b   % 2em空格
a\, b       % 小空格
a\! b       % 负空格
```

---

## 🔧 编译命令

```bash
# XeLaTeX编译（支持中文）
xelatex main.tex

# 带参考文献的完整编译
xelatex main.tex
bibtex main
xelatex main.tex
xelatex main.tex

# 清理临时文件
rm *.aux *.log *.out *.toc *.bbl *.blg
```

---

## 📚 更多资源

- **LaTeX符号查询**：http://detexify.kirelabs.org/classify.html
- **表格生成器**：https://www.tablesgenerator.com/
- **公式编辑器**：https://www.codecogs.com/latex/eqneditor.php
- **Overleaf文档**：https://www.overleaf.com/learn

---

**💡 建议**：打印或保存本速查表，写论文时随时查阅！

