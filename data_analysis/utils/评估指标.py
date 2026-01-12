"""
模型评估指标工具函数
提供分类和回归任务的常用评估指标
"""

import numpy as np
import pandas as pd
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, classification_report,
    mean_squared_error, mean_absolute_error, r2_score
)
import matplotlib.pyplot as plt
import seaborn as sns

# ==================== 设置中文字体 ====================
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']  # Mac系统
# plt.rcParams['font.sans-serif'] = ['SimHei']  # Windows系统
plt.rcParams['axes.unicode_minus'] = False


# ==================== 分类模型评估 ====================
def evaluate_classification(y_true, y_pred, labels=None, print_report=True):
    """
    评估分类模型性能
    
    参数:
        y_true: 真实标签（数组）
        y_pred: 预测标签（数组）
        labels: 类别标签列表（可选）
        print_report: 是否打印详细报告
    
    返回:
        字典，包含所有评估指标
    """
    # 计算各项指标
    metrics = {
        '准确率 (Accuracy)': accuracy_score(y_true, y_pred),
        '精确率 (Precision)': precision_score(y_true, y_pred, average='weighted', zero_division=0),
        '召回率 (Recall)': recall_score(y_true, y_pred, average='weighted', zero_division=0),
        'F1分数 (F1-Score)': f1_score(y_true, y_pred, average='weighted', zero_division=0)
    }
    
    if print_report:
        print("=" * 60)
        print("📊 分类模型评估结果")
        print("=" * 60)
        
        # 打印各项指标
        for metric_name, metric_value in metrics.items():
            print(f"\n{metric_name}: {metric_value:.4f}")
        
        # 打印详细分类报告
        print("\n" + "-" * 60)
        print("详细分类报告:")
        print("-" * 60)
        print(classification_report(y_true, y_pred, target_names=labels, zero_division=0))
        
        # 混淆矩阵
        cm = confusion_matrix(y_true, y_pred)
        print("\n混淆矩阵:")
        print(cm)
    
    return metrics


# ==================== 绘制混淆矩阵 ====================
def plot_confusion_matrix(y_true, y_pred, labels=None, save_path=None):
    """
    绘制混淆矩阵热力图
    
    参数:
        y_true: 真实标签
        y_pred: 预测标签
        labels: 类别标签（可选）
        save_path: 保存路径（可选）
    """
    # 计算混淆矩阵
    cm = confusion_matrix(y_true, y_pred)
    
    # 创建图表
    plt.figure(figsize=(8, 6), dpi=300)
    
    # 绘制热力图
    sns.heatmap(
        cm,
        annot=True,  # 显示数值
        fmt='d',  # 整数格式
        cmap='Blues',  # 颜色映射
        xticklabels=labels if labels else 'auto',
        yticklabels=labels if labels else 'auto',
        cbar_kws={'label': '样本数量'}
    )
    
    plt.title('混淆矩阵', fontsize=14, fontweight='bold', pad=20)
    plt.xlabel('预测标签', fontsize=12, fontweight='bold')
    plt.ylabel('真实标签', fontsize=12, fontweight='bold')
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"✅ 混淆矩阵已保存: {save_path}")
    
    plt.show()


# ==================== 回归模型评估 ====================
def evaluate_regression(y_true, y_pred, print_report=True):
    """
    评估回归模型性能
    
    参数:
        y_true: 真实值（数组）
        y_pred: 预测值（数组）
        print_report: 是否打印报告
    
    返回:
        字典，包含所有评估指标
    """
    # 计算各项指标
    mse = mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    
    # 计算MAPE（平均绝对百分比误差）
    mape = np.mean(np.abs((y_true - y_pred) / y_true)) * 100
    
    metrics = {
        'MSE (均方误差)': mse,
        'RMSE (均方根误差)': rmse,
        'MAE (平均绝对误差)': mae,
        'R² (决定系数)': r2,
        'MAPE (%) (平均绝对百分比误差)': mape
    }
    
    if print_report:
        print("=" * 60)
        print("📊 回归模型评估结果")
        print("=" * 60)
        
        for metric_name, metric_value in metrics.items():
            print(f"\n{metric_name}: {metric_value:.4f}")
        
        # 解释R²
        print("\n" + "-" * 60)
        print("R²解释:")
        if r2 > 0.9:
            print("  ✅ 优秀 (R² > 0.9): 模型拟合非常好")
        elif r2 > 0.7:
            print("  ✅ 良好 (R² > 0.7): 模型拟合较好")
        elif r2 > 0.5:
            print("  ⚠️  一般 (R² > 0.5): 模型有一定预测能力")
        else:
            print("  ❌ 较差 (R² < 0.5): 模型预测能力较弱")
    
    return metrics


# ==================== 绘制回归结果 ====================
def plot_regression_results(y_true, y_pred, save_path=None):
    """
    绘制回归模型的预测结果对比图
    
    参数:
        y_true: 真实值
        y_pred: 预测值
        save_path: 保存路径（可选）
    """
    fig, axes = plt.subplots(1, 2, figsize=(14, 6), dpi=300)
    
    # 图1: 真实值vs预测值散点图
    ax1 = axes[0]
    ax1.scatter(y_true, y_pred, alpha=0.6, s=50, edgecolors='black', linewidth=0.5)
    
    # 绘制理想直线（y=x）
    min_val = min(y_true.min(), y_pred.min())
    max_val = max(y_true.max(), y_pred.max())
    ax1.plot([min_val, max_val], [min_val, max_val], 'r--', linewidth=2, label='理想预测线')
    
    ax1.set_xlabel('真实值', fontsize=12, fontweight='bold')
    ax1.set_ylabel('预测值', fontsize=12, fontweight='bold')
    ax1.set_title('真实值 vs 预测值', fontsize=14, fontweight='bold')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # 图2: 残差图
    ax2 = axes[1]
    residuals = y_true - y_pred
    ax2.scatter(y_pred, residuals, alpha=0.6, s=50, edgecolors='black', linewidth=0.5)
    ax2.axhline(y=0, color='r', linestyle='--', linewidth=2, label='零残差线')
    
    ax2.set_xlabel('预测值', fontsize=12, fontweight='bold')
    ax2.set_ylabel('残差', fontsize=12, fontweight='bold')
    ax2.set_title('残差分布图', fontsize=14, fontweight='bold')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"✅ 回归结果图已保存: {save_path}")
    
    plt.show()


# ==================== 交叉验证评估 ====================
def evaluate_with_cv(model, X, y, cv=5, scoring='accuracy'):
    """
    使用交叉验证评估模型
    
    参数:
        model: 机器学习模型
        X: 特征数据
        y: 标签数据
        cv: 折数（默认5折）
        scoring: 评分标准（'accuracy', 'f1', 'r2'等）
    
    返回:
        交叉验证分数
    """
    from sklearn.model_selection import cross_val_score
    
    print(f"🔄 正在进行{cv}折交叉验证...")
    
    # 执行交叉验证
    scores = cross_val_score(
        model,  # 模型
        X,  # 特征
        y,  # 标签
        cv=cv,  # 折数
        scoring=scoring  # 评分标准
    )
    
    print(f"\n✅ 交叉验证完成")
    print(f"   各折得分: {scores}")
    print(f"   平均得分: {scores.mean():.4f} (±{scores.std():.4f})")
    
    return scores


# ==================== 使用示例 ====================
if __name__ == "__main__":
    print("=" * 60)
    print("评估指标工具 - 使用示例")
    print("=" * 60)
    
    # ========== 分类任务示例 ==========
    print("\n【示例1: 分类任务评估】")
    print("-" * 60)
    
    # 生成示例数据
    np.random.seed(42)
    y_true_cls = np.random.randint(0, 3, 100)  # 3个类别
    y_pred_cls = y_true_cls.copy()
    # 添加一些预测错误
    errors = np.random.choice(100, 20, replace=False)
    y_pred_cls[errors] = np.random.randint(0, 3, 20)
    
    # 评估分类模型
    metrics_cls = evaluate_classification(
        y_true_cls,
        y_pred_cls,
        labels=['类别A', '类别B', '类别C'],
        print_report=True
    )
    
    # 绘制混淆矩阵
    plot_confusion_matrix(
        y_true_cls,
        y_pred_cls,
        labels=['类别A', '类别B', '类别C'],
        save_path='混淆矩阵示例.png'
    )
    
    # ========== 回归任务示例 ==========
    print("\n\n【示例2: 回归任务评估】")
    print("-" * 60)
    
    # 生成示例数据
    y_true_reg = np.random.randn(100) * 10 + 50
    y_pred_reg = y_true_reg + np.random.randn(100) * 3  # 添加预测误差
    
    # 评估回归模型
    metrics_reg = evaluate_regression(
        y_true_reg,
        y_pred_reg,
        print_report=True
    )
    
    # 绘制回归结果
    plot_regression_results(
        y_true_reg,
        y_pred_reg,
        save_path='回归结果示例.png'
    )
    
    print("\n" + "=" * 60)
    print("✅ 示例运行完成！")
    print("=" * 60)
    
    print("\n💡 使用提示:")
    print("  分类任务: 使用 evaluate_classification() 和 plot_confusion_matrix()")
    print("  回归任务: 使用 evaluate_regression() 和 plot_regression_results()")
    print("  交叉验证: 使用 evaluate_with_cv()")

