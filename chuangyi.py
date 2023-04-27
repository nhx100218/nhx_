# 专注时钟，每25分钟提醒一次休息
import time

# 设置专注时间为25分钟
focus_time = 25 * 60

# 设置开始时间为当前时间
start_time = time.time()

# 设置结束时间为开始时间加上专注时间
end_time = start_time + focus_time

# 循环检查当前时间是否达到结束时间
while True:
    # 获取当前时间
    current_time = time.time()
    # 如果当前时间大于或等于结束时间，说明专注时间已经结束
    if current_time >= end_time:
        # 打印提醒信息
        print("专注时间结束，休息一下吧！")
        # 跳出循环
        break
    # 否则，继续循环
    else:
        # 等待一秒
        time.sleep(1)
