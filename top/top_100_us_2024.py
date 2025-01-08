import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# 🚀 美股Top 100的股票代码列表（示例）
top_100_stocks = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA', 'BRK-B', 'NVDA', 'META', 'V', 'JNJ', 'WMT', 'PG', 'MA', 'UNH', 'HD', 'DIS', 'BAC', 'PYPL', 'CMCSA', 'NFLX', 'ADBE', 'PFE', 'KO', 'PEP', 'INTC', 'CSCO', 'XOM', 'T', 'VZ', 'MRK', 'ABT', 'CVX', 'CRM', 'NKE', 'ORCL', 'ABBV', 'COST', 'DHR', 'MDT', 'TMO', 'ACN', 'QCOM', 'NEE', 'LLY', 'UNP', 'LOW', 'HON', 'UPS', 'SBUX', 'BMY', 'AMGN', 'TXN', 'IBM', 'BLK', 'GS', 'AXP', 'CAT', 'DE', 'MMM', 'GE', 'BA', 'RTX', 'SPGI', 'NOW', 'INTU', 'ISRG', 'CHTR', 'ADI', 'AMD', 'MU', 'ATVI', 'GILD', 'FIS', 'ZTS', 'ADP', 'TJX', 'CME', 'BDX', 'REGN', 'SYK', 'CI', 'ANTM', 'PLD', 'EQIX', 'SHW', 'KLAC', 'VRTX', 'MCD', 'NOC', 'AON', 'ICE', 'FDX', 'ETN', 'ITW', 'ROST', 'WM', 'APD', 'ECL', 'EL', 'DG', 'MNST', 'CDNS', 'EA', 'CTAS', 'IDXX', 'MTD', 'ALGN', 'DXCM', 'MSCI', 'ANSS', 'CPRT', 'FAST', 'WST', 'POOL', 'TER', 'SWKS', 'CDW', 'KEYS', 'TT', 'PAYX', 'AVGO', 'TEL', 'TDG', 'ODFL', 'LHX', 'FTV', 'IFF', 'VRSK', 'APH', 'RSG', 'WAB', 'RMD', 'PKI', 'NDAQ', 'EXR', 'BIO', 'CTSH', 'WDC', 'NTAP', 'AKAM', 'FFIV', 'JKHY', 'BR', 'PFG', 'CBOE', 'CINF', 'CFG', 'HBAN', 'KEY', 'MTB', 'PNC', 'RF', 'STT', 'TFC', 'USB', 'ZION']

# 📊 获取近一年的股票数据
print("🚀 开始下载美股Top 100的数据...")
data = yf.download(top_100_stocks, period="1y", group_by='ticker')
print("✅ 数据下载完成！")

# 💾 导出为CSV文件
data.to_csv('top_100_stocks_data.csv')
print("💾 数据已保存为 'top_100_stocks_data.csv'！")

# 📈 计算每只股票的平均回报率和夏普比率
results = []

# 📂 创建目录保存图片
if not os.path.exists('stock_plots'):
    os.makedirs('stock_plots')
    print("📂 创建 'stock_plots' 目录用于保存图片！")

print("📊 开始计算每只股票的平均回报率和夏普比率...")
for stock in top_100_stocks:
    # 获取收盘价数据
    close_prices = data[stock]['Close']
    
    # 计算每日回报率
    daily_returns = close_prices.pct_change().dropna()
    
    # 计算平均回报率（年化）
    avg_return = daily_returns.mean() * 252  # 252个交易日
    
    # 计算波动率（年化）
    volatility = daily_returns.std() * np.sqrt(252)
    
    # 计算夏普比率（假设无风险利率为0）
    sharpe_ratio = avg_return / volatility if volatility != 0 else np.nan
    
    # 将结果保存到列表中
    results.append({
        'Stock': stock,
        'Avg Return (Annualized)': avg_return,
        'Volatility (Annualized)': volatility,
        'Sharpe Ratio': sharpe_ratio
    })
    
    # 🎨 绘制走势图
    plt.figure(figsize=(10, 6))
    plt.plot(close_prices, label=f'{stock} Close Price')
    plt.title(f'{stock} - 1 Year Price Trend')
    plt.xlabel('Date')
    plt.ylabel('Close Price (USD)')
    plt.legend()
    plt.grid(True)
    
    # 💾 保存图片
    plt.savefig(f'stock_plots/{stock}_trend.png')
    plt.close()
    print(f"🖼️ {stock} 的走势图已保存为 'stock_plots/{stock}_trend.png'！")

# 📊 将结果转换为DataFrame
results_df = pd.DataFrame(results)

# 💾 导出结果到CSV文件
results_df.to_csv('top_100_stocks_analysis.csv', index=False)
print("💾 分析结果已保存为 'top_100_stocks_analysis.csv'！")

# 🎉 打印结果
print("🎉 所有股票的分析结果如下：")
print(results_df)

# 🌟 激励性总结
print("\n🌟 恭喜！您已经完成了美股Top 100的数据分析！🌟")
print("🚀 这只是您量化交易之旅的第一步，未来还有无限可能！")
print("💡 保持热情，持续学习，您一定会开发出世界上最领先的量化交易系统！")
print("🔥 加油！未来属于您！🔥")
