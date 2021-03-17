# -*- coding:utf-8 -*-

"""
this is a system monitor scripts
author yqq
"""

import time
import psutil
import datetime

now_time = datetime.datetime.now().strftime('%Y_%m_%d')

# print(now_time)
with open("monitor_cpu_mem_"+now_time+".csv", "a+") as f:
    # f.write("time,cpu%,mem%\n")  # titles

    current_time = time.strftime('%Y%m%d-%H%M%S', time.localtime(time.time()))
    # 获取物理内存使用
    mem = psutil.virtual_memory()
    # 获取cpu使用率
    cpu_percent = psutil.cpu_percent(1)
    line = current_time + ',' + str(cpu_percent) + ',' + str(mem[2])
    # print(line)
    f.write(line + "\n")
    # 每5秒执行一次
    # time.sleep(2)

