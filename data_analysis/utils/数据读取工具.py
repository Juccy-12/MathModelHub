"""
数据读取工具函数
支持多种数据格式：CSV、Excel、JSON、SQL等
"""

import pandas as pd
import numpy as np
import json

# ==================== CSV文件读取 ====================
def read_csv_file(file_path, encoding='utf-8'):
    """
    读取CSV文件
    
    参数:
        file_path: 文件路径（如 'data.csv'）
        encoding: 编码格式（'utf-8', 'gbk', 'gb2312'）
    
    返回:
        DataFrame
    """
    try:
        # 尝试读取CSV文件
        data = pd.read_csv(
            file_path,  # 文件路径
            encoding=encoding  # 编码格式
        )
        
        print(f"✅ 成功读取文件: {file_path}")
        print(f"   数据形状: {data.shape} (行数×列数)")
        print(f"   列名: {list(data.columns)}")
        
        return data
    
    except UnicodeDecodeError:
        # 如果编码错误，尝试其他编码
        print(f"❌ 编码'{encoding}'失败，尝试'gbk'编码...")
        return read_csv_file(file_path, encoding='gbk')
    
    except FileNotFoundError:
        print(f"❌ 文件不存在: {file_path}")
        return None
    
    except Exception as e:
        print(f"❌ 读取失败: {e}")
        return None


# ==================== Excel文件读取 ====================
def read_excel_file(file_path, sheet_name=0):
    """
    读取Excel文件
    
    参数:
        file_path: 文件路径（如 'data.xlsx'）
        sheet_name: 工作表名称或索引（默认第一个工作表）
                    0表示第一个, 1表示第二个, 或直接用'Sheet1'
    
    返回:
        DataFrame
    """
    try:
        data = pd.read_excel(
            file_path,  # 文件路径
            sheet_name=sheet_name,  # 工作表
            engine='openpyxl'  # Excel引擎
        )
        
        print(f"✅ 成功读取Excel: {file_path}")
        print(f"   工作表: {sheet_name}")
        print(f"   数据形状: {data.shape}")
        print(f"   列名: {list(data.columns)}")
        
        return data
    
    except FileNotFoundError:
        print(f"❌ 文件不存在: {file_path}")
        return None
    
    except Exception as e:
        print(f"❌ 读取失败: {e}")
        print("   提示: 需要安装openpyxl: pip install openpyxl")
        return None


# ==================== 读取Excel所有工作表 ====================
def read_all_excel_sheets(file_path):
    """
    读取Excel文件的所有工作表
    
    参数:
        file_path: 文件路径
    
    返回:
        字典 {工作表名: DataFrame}
    """
    try:
        # 读取所有工作表
        all_sheets = pd.read_excel(
            file_path,
            sheet_name=None,  # None表示读取所有工作表
            engine='openpyxl'
        )
        
        print(f"✅ 成功读取Excel: {file_path}")
        print(f"   工作表数量: {len(all_sheets)}")
        print(f"   工作表名称: {list(all_sheets.keys())}")
        
        # 显示每个工作表的信息
        for sheet_name, sheet_data in all_sheets.items():
            print(f"\n   工作表'{sheet_name}': {sheet_data.shape}")
        
        return all_sheets
    
    except Exception as e:
        print(f"❌ 读取失败: {e}")
        return None


# ==================== JSON文件读取 ====================
def read_json_file(file_path, orient='records'):
    """
    读取JSON文件
    
    参数:
        file_path: 文件路径
        orient: JSON格式（'records', 'index', 'columns'）
                'records': [{col1:val, col2:val}, ...]
                'index': {index: {col1:val, col2:val}, ...}
    
    返回:
        DataFrame
    """
    try:
        data = pd.read_json(
            file_path,
            orient=orient,
            encoding='utf-8'
        )
        
        print(f"✅ 成功读取JSON: {file_path}")
        print(f"   数据形状: {data.shape}")
        
        return data
    
    except Exception as e:
        print(f"❌ 读取失败: {e}")
        return None


# ==================== 从数据库读取 ====================
def read_from_database(sql_query, connection_string):
    """
    从数据库读取数据
    
    参数:
        sql_query: SQL查询语句
        connection_string: 数据库连接字符串
            SQLite示例: 'sqlite:///database.db'
            MySQL示例: 'mysql://user:password@host:port/database'
    
    返回:
        DataFrame
    """
    try:
        from sqlalchemy import create_engine
        
        # 创建数据库引擎
        engine = create_engine(connection_string)
        
        # 执行SQL查询
        data = pd.read_sql(
            sql_query,  # SQL查询
            con=engine  # 数据库连接
        )
        
        print(f"✅ 成功从数据库读取数据")
        print(f"   数据形状: {data.shape}")
        
        return data
    
    except Exception as e:
        print(f"❌ 读取失败: {e}")
        print("   提示: 需要安装sqlalchemy: pip install sqlalchemy")
        return None


# ==================== 自动识别文件类型并读取 ====================
def read_file_auto(file_path):
    """
    自动识别文件类型并读取
    
    参数:
        file_path: 文件路径
    
    返回:
        DataFrame
    """
    import os
    
    # 获取文件扩展名
    _, ext = os.path.splitext(file_path)
    ext = ext.lower()
    
    print(f"📂 正在读取: {file_path}")
    print(f"   文件类型: {ext}")
    
    # 根据扩展名选择读取方法
    if ext == '.csv':
        return read_csv_file(file_path)
    
    elif ext in ['.xlsx', '.xls']:
        return read_excel_file(file_path)
    
    elif ext == '.json':
        return read_json_file(file_path)
    
    elif ext == '.txt':
        # 尝试作为CSV读取
        return read_csv_file(file_path)
    
    else:
        print(f"❌ 不支持的文件类型: {ext}")
        print("   支持的类型: .csv, .xlsx, .xls, .json, .txt")
        return None


# ==================== 快速查看数据 ====================
def quick_preview(data, n_rows=5):
    """
    快速查看数据的基本信息
    
    参数:
        data: DataFrame
        n_rows: 显示的行数
    """
    if data is None:
        print("❌ 数据为空")
        return
    
    print("\n" + "=" * 60)
    print("📊 数据预览")
    print("=" * 60)
    
    # 1. 数据形状
    print(f"\n1. 数据形状: {data.shape} (行×列)")
    
    # 2. 列信息
    print(f"\n2. 列信息:")
    print(data.dtypes)
    
    # 3. 前几行
    print(f"\n3. 前{n_rows}行数据:")
    print(data.head(n_rows))
    
    # 4. 基本统计
    print(f"\n4. 数值列统计:")
    print(data.describe())
    
    # 5. 缺失值
    missing = data.isnull().sum()
    if missing.any():
        print(f"\n5. 缺失值:")
        print(missing[missing > 0])
    else:
        print(f"\n5. 缺失值: 无缺失")


# ==================== 使用示例 ====================
if __name__ == "__main__":
    print("=" * 60)
    print("数据读取工具 - 使用示例")
    print("=" * 60)
    
    # 示例1: 读取CSV文件
    print("\n示例1: 读取CSV文件")
    print("-" * 60)
    # data_csv = read_csv_file('data.csv')  # 替换成你的文件路径
    
    # 示例2: 读取Excel文件
    print("\n示例2: 读取Excel文件")
    print("-" * 60)
    # data_excel = read_excel_file('data.xlsx', sheet_name='Sheet1')
    
    # 示例3: 读取Excel所有工作表
    print("\n示例3: 读取Excel所有工作表")
    print("-" * 60)
    # all_sheets = read_all_excel_sheets('data.xlsx')
    
    # 示例4: 自动识别文件类型
    print("\n示例4: 自动识别文件类型")
    print("-" * 60)
    # data = read_file_auto('data.csv')  # 自动识别.csv, .xlsx等
    
    # 示例5: 快速预览数据
    print("\n示例5: 快速预览数据")
    print("-" * 60)
    
    # 创建示例数据
    example_data = pd.DataFrame({
        '姓名': ['张三', '李四', '王五'],
        '年龄': [25, 30, 35],
        '收入': [50000, 60000, 70000]
    })
    
    quick_preview(example_data, n_rows=3)
    
    print("\n" + "=" * 60)
    print("使用提示:")
    print("  1. 根据文件类型选择对应的读取函数")
    print("  2. 如果不确定类型，使用 read_file_auto()")
    print("  3. 读取后使用 quick_preview() 快速查看数据")
    print("=" * 60)

