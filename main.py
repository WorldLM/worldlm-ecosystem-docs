# main.py

import sys
from ainalyst_crew import AInalystCrew

def run():
    inputs = {
        'symbol': input("请输入交易对 (例如，BTCUSDT): "),
        'interval': input("请输入时间间隔 (例如，1h, 4h, 1d): ")
    }
    return AInalystCrew().crew().kickoff(inputs=inputs)

if __name__ == "__main__":
    print("## 欢迎使用 AInalyst")
    print('-------------------------------')
    result = run()
    print("\n\n########################")
    print("## 市场分析报告")
    print("########################\n")
    print(result)