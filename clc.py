# 导入time模块
import time

# 设置休息时长（分钟）
break_time = 5

# 询问用户想要专注的时长（分钟）
focus_time = int(input("你想要专注多少分钟？"))

# 询问用户想要进行多少个周期（次数）
cycles = int(input("你想要进行多少个周期？"))

# 定义一个函数，用于显示倒计时
def countdown(minutes):
    # 将分钟转换为秒数
    seconds = minutes * 60
    # 循环减少秒数，直到为零
    while seconds > 0:
        # 将秒数格式化为分:秒的形式
        time_format = f"{seconds // 60}:{seconds % 60:02d}"
        # 打印倒计时
        print(time_format, end="\r")
        # 暂停一秒
        time.sleep(1)
        # 减少一秒
        seconds -= 1

# 开始专注时钟
print("开始专注时钟！")
# 循环进行专注和休息
for i in range(cycles):
    # 打印当前周期
    print(f"第{i + 1}个周期：")
    # 开始专注
    print(f"开始专注{focus_time}分钟！")
    # 调用倒计时函数
    countdown(focus_time)
    # 提示专注结束
    print(f"专注结束！")
    # 判断是否是最后一个周期
    if i == cycles - 1:
        # 提示全部完成
        print("恭喜你，全部完成！")
        # 结束程序
        break
    # 开始休息
    print(f"开始休息{break_time}分钟！")
    # 调用倒计时函数
    countdown(break_time)
    # 提示休息结束
    print(f"休息结束！")
