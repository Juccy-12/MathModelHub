"""
时间数据处理工具函数
处理日期时间格式转换、特征提取等
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# ==================== 日期格式转换 ====================
def parse_datetime(date_string, format='auto'):
    """
    将字符串转换为datetime对象
    
    参数:
        date_string: 日期字符串（如 '2023-01-15', '2023/01/15 10:30:00'）
        format: 日期格式（'auto'自动识别, 或指定格式如'%Y-%m-%d'）
    
    返回:
        datetime对象
    """
    if format == 'auto':
        # 自动识别日期格式
        try:
            return pd.to_datetime(date_string)
        except Exception as e:
            print(f"❌ 无法解析日期: {date_string}")
            print(f"   错误: {e}")
            return None
    else:
        # 使用指定格式
        try:
            return datetime.strptime(date_string, format)
        except Exception as e:
            print(f"❌ 日期格式不匹配: {date_string}")
            print(f"   期望格式: {format}")
            return None


# ==================== 批量转换DataFrame中的日期列 ====================
def convert_datetime_column(data, column_name, format='auto'):
    """
    将DataFrame中的某列转换为datetime类型
    
    参数:
        data: DataFrame
        column_name: 列名
        format: 日期格式
    
    返回:
        转换后的DataFrame
    """
    try:
        data[column_name] = pd.to_datetime(data[column_name], format=format if format != 'auto' else None)
        print(f"✅ 列'{column_name}'已转换为datetime类型")
        return data
    except Exception as e:
        print(f"❌ 转换失败: {e}")
        return data


# ==================== 从日期中提取特征 ====================
def extract_datetime_features(data, datetime_column):
    """
    从日期时间列中提取有用的特征
    
    参数:
        data: DataFrame
        datetime_column: 日期时间列名
    
    返回:
        添加了时间特征的DataFrame
    """
    # 确保是datetime类型
    if data[datetime_column].dtype != 'datetime64[ns]':
        data = convert_datetime_column(data, datetime_column)
    
    # 提取各种时间特征
    data[f'{datetime_column}_年'] = data[datetime_column].dt.year  # 年份
    data[f'{datetime_column}_月'] = data[datetime_column].dt.month  # 月份（1-12）
    data[f'{datetime_column}_日'] = data[datetime_column].dt.day  # 日期（1-31）
    data[f'{datetime_column}_星期'] = data[datetime_column].dt.dayofweek  # 星期几（0=周一, 6=周日）
    data[f'{datetime_column}_小时'] = data[datetime_column].dt.hour  # 小时（0-23）
    data[f'{datetime_column}_季度'] = data[datetime_column].dt.quarter  # 季度（1-4）
    data[f'{datetime_column}_是否周末'] = data[datetime_column].dt.dayofweek.isin([5, 6]).astype(int)  # 是否周末
    
    # 年中第几天
    data[f'{datetime_column}_年中第几天'] = data[datetime_column].dt.dayofyear
    
    # 年中第几周
    data[f'{datetime_column}_年中第几周'] = data[datetime_column].dt.isocalendar().week
    
    print(f"✅ 已从'{datetime_column}'列提取时间特征:")
    print(f"   - 年、月、日、星期、小时、季度")
    print(f"   - 是否周末、年中第几天、年中第几周")
    
    return data


# ==================== 计算日期差异 ====================
def calculate_date_diff(date1, date2, unit='days'):
    """
    计算两个日期之间的差异
    
    参数:
        date1: 第一个日期（datetime对象或字符串）
        date2: 第二个日期
        unit: 单位（'days', 'hours', 'minutes', 'seconds'）
    
    返回:
        时间差（数值）
    """
    # 转换为datetime对象
    if isinstance(date1, str):
        date1 = pd.to_datetime(date1)
    if isinstance(date2, str):
        date2 = pd.to_datetime(date2)
    
    # 计算差异
    diff = date2 - date1
    
    # 根据单位返回结果
    if unit == 'days':
        return diff.days
    elif unit == 'hours':
        return diff.total_seconds() / 3600
    elif unit == 'minutes':
        return diff.total_seconds() / 60
    elif unit == 'seconds':
        return diff.total_seconds()
    else:
        print(f"❌ 不支持的单位: {unit}")
        return None


# ==================== 生成日期范围 ====================
def generate_date_range(start_date, end_date, freq='D'):
    """
    生成日期范围
    
    参数:
        start_date: 开始日期（字符串或datetime）
        end_date: 结束日期
        freq: 频率（'D'每天, 'W'每周, 'M'每月, 'H'每小时）
    
    返回:
        日期范围（DatetimeIndex）
    """
    date_range = pd.date_range(
        start=start_date,
        end=end_date,
        freq=freq
    )
    
    print(f"✅ 生成日期范围:")
    print(f"   开始: {date_range[0]}")
    print(f"   结束: {date_range[-1]}")
    print(f"   共{len(date_range)}个日期")
    
    return date_range


# ==================== 日期格式化 ====================
def format_datetime(dt, format='%Y-%m-%d'):
    """
    将datetime对象格式化为字符串
    
    参数:
        dt: datetime对象
        format: 格式字符串
                常用格式:
                '%Y-%m-%d' → '2023-01-15'
                '%Y/%m/%d' → '2023/01/15'
                '%Y-%m-%d %H:%M:%S' → '2023-01-15 10:30:00'
                '%Y年%m月%d日' → '2023年01月15日'
    
    返回:
        格式化的字符串
    """
    if isinstance(dt, str):
        dt = pd.to_datetime(dt)
    
    return dt.strftime(format)


# ==================== 按时间分组聚合 ====================
def resample_timeseries(data, datetime_column, freq='D', agg_func='mean'):
    """
    按时间频率重采样和聚合时间序列数据
    
    参数:
        data: DataFrame
        datetime_column: 时间列名
        freq: 重采样频率（'D'每天, 'W'每周, 'M'每月, 'H'每小时）
        agg_func: 聚合函数（'mean', 'sum', 'count', 'max', 'min'）
    
    返回:
        重采样后的DataFrame
    """
    # 设置时间列为索引
    data_copy = data.copy()
    data_copy[datetime_column] = pd.to_datetime(data_copy[datetime_column])
    data_copy = data_copy.set_index(datetime_column)
    
    # 重采样
    if agg_func == 'mean':
        resampled = data_copy.resample(freq).mean()
    elif agg_func == 'sum':
        resampled = data_copy.resample(freq).sum()
    elif agg_func == 'count':
        resampled = data_copy.resample(freq).count()
    elif agg_func == 'max':
        resampled = data_copy.resample(freq).max()
    elif agg_func == 'min':
        resampled = data_copy.resample(freq).min()
    else:
        print(f"❌ 不支持的聚合函数: {agg_func}")
        return data
    
    print(f"✅ 时间序列已重采样:")
    print(f"   原始数据: {len(data)}行")
    print(f"   重采样后: {len(resampled)}行")
    print(f"   频率: {freq}, 聚合方式: {agg_func}")
    
    return resampled.reset_index()


# ==================== 使用示例 ====================
if __name__ == "__main__":
    print("=" * 60)
    print("时间处理工具 - 使用示例")
    print("=" * 60)
    
    # 示例1: 日期格式转换
    print("\n示例1: 日期格式转换")
    print("-" * 60)
    date_str = "2023-01-15 10:30:00"
    dt = parse_datetime(date_str)
    print(f"字符串: {date_str}")
    print(f"转换后: {dt}")
    
    # 示例2: 创建示例DataFrame
    print("\n示例2: 从日期提取特征")
    print("-" * 60)
    dates = pd.date_range('2023-01-01', periods=10, freq='D')
    data = pd.DataFrame({
        '日期': dates,
        '销售额': np.random.randint(1000, 5000, 10)
    })
    
    print("原始数据:")
    print(data)
    
    # 提取时间特征
    data = extract_datetime_features(data, '日期')
    print("\n提取特征后:")
    print(data[['日期', '日期_年', '日期_月', '日期_星期', '日期_是否周末']].head())
    
    # 示例3: 计算日期差异
    print("\n示例3: 计算日期差异")
    print("-" * 60)
    date1 = "2023-01-01"
    date2 = "2023-01-15"
    diff_days = calculate_date_diff(date1, date2, unit='days')
    print(f"从 {date1} 到 {date2} 相差 {diff_days} 天")
    
    # 示例4: 生成日期范围
    print("\n示例4: 生成日期范围")
    print("-" * 60)
    date_range = generate_date_range('2023-01-01', '2023-01-31', freq='D')
    print(f"前5个日期: {date_range[:5]}")
    
    # 示例5: 时间序列重采样
    print("\n示例5: 时间序列重采样")
    print("-" * 60)
    # 创建每小时数据
    hourly_data = pd.DataFrame({
        '时间': pd.date_range('2023-01-01', periods=72, freq='H'),
        '温度': np.random.randn(72) * 5 + 20
    })
    
    print(f"原始数据（每小时）: {len(hourly_data)}行")
    
    # 重采样为每天数据
    daily_data = resample_timeseries(hourly_data, '时间', freq='D', agg_func='mean')
    print(f"\n重采样后的数据:")
    print(daily_data.head())
    
    print("\n" + "=" * 60)
    print("✅ 所有示例运行完成！")
    print("=" * 60)
