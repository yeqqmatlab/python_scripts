# -*- coding:utf-8 -*-

"""
this is a system monitor scripts
author yqq
"""

import time
import psutil
import datetime
import os

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

log1 = "ping_ip247_info_"+now_time+".log"
os.system('date >> ' + log1)
os.system('ping -c 1 -w 1 ip247 >> ' + log1)

log2 = "ping_baidu_info_"+now_time+".log"
os.system('date >> ' + log2)
os.system('ping -c 1 -w 1 www.baidu.com >> ' + log2)


