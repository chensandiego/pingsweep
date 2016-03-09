

import threading
import time
import socket, subprocess,sys
import _thread
import collections
from datetime import datetime

'''section 1
input your ip range
the network address is the full range ip like 192.168.0.1
starting number is which host ip you want to start the scanning
Last number is the last host ip you want to complete the scanning 

you can adjust tn number. The lower numbers mean more threading which will run faster but consume more CPU
tn =10 will take less than 11 seconds to scan 192.168.0.1-254 compare to nmap which uses 16 seconds
''' 
net = input("Enter the Network Address ")
st1 = int(input("Enter the starting Number  "))
en1 = int(input("Enter the last Number "))
en1=en1+1
dic = collections.OrderedDict()
net1= net.split('.')
a = '.'
net2 = net1[0]+a+net1[1]+a+net1[2]+a
t1= datetime.now()
'''section 2'''
class myThread (threading.Thread):
  def __init__(self,st,en):
    threading.Thread.__init__(self)
    self.st = st
    self.en = en
  def run(self):
    run1(self.st,self.en)

'''section 3'''
def scan(addr):
  sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  socket.setdefaulttimeout(1)
  result = sock.connect_ex((addr,135))
  if result==0:
    sock.close()
    return 1
  else :
    sock.close()

def run1(st1,en1):
  for ip in range(st1,en1):
    addr = net2+str(ip)
    if scan(addr):
      dic[ip]= addr
'''section 4'''
total_ip =en1-st1
tn =10  # number of ip handled by one thread
total_thread = total_ip/tn
total_thread=total_thread+1
threads= []

for i in range(int(total_thread)):
	 
	en = st1+tn
	if(en >en1):
		en =en1
	thread = myThread(st1,en)
	thread.start()
	threads.append(thread)
	st1 =en
	 
print ("\t Number of Threads active:", threading.activeCount())
for t in threads:
  t.join()
print ("Exiting Main Thread")
dict = collections.OrderedDict(sorted(dic.items()))
for key in dict:
  print (dict[key],"-->" "Live")
t2= datetime.now()
total =t2-t1
print ("scanning complete in " , total)