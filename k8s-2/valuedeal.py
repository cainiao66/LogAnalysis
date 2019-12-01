#处理value.log  转换为时间差
from datetime import datetime 
import numpy as np
with open("value.log","r")as valuedeal:
    values=valuedeal.readlines()

dealvalue=[]
for i in range(len(values)-1):
    v1=values[i][:-1].split(" ")
    v2=values[i+1][:-1].split(" ")
    time1=datetime(int(v1[0]),int(v1[1]),int(v1[2]),hour=int(v1[3]),minute=int(v1[4]),second=int(v1[5]),microsecond=int(v1[6]))
    time2=datetime(int(v2[0]),int(v2[1]),int(v2[2]),hour=int(v2[3]),minute=int(v2[4]),second=int(v2[5]),microsecond=int(v2[6]))
    time=(time2.day-time1.day)*86400000+(time2.hour-time1.hour)*3600000+(time2.minute-time1.minute)*60000+(time2.second-time1.second)*1000+(time2.microsecond-time1.microsecond)
    v=str(time)+" "+v2[7]+" "+v2[8]+" "+v2[9]+"\n"
    dealvalue.append(v)

with open("dealedvalue.log","a+")as dvalue:
    for i in dealvalue:
        dvalue.write(i)

#做标准化

with open("dealedvalue.log","r")as v:
    lines=v.readlines()
    #取出时间  
    t=[]
    #取出进程
    process=[]
    #取出端口
    port=[]
    #取出线程
    thread=[]
    for i in lines:
        strline=i[:-1].split(" ")  #去除最后的回车 然后用空格分离
        t.append(int(strline[0]))
        process.append(int(strline[1]))
        port.append(int(strline[2]))
        thread.append(int(strline[3]))

t_mean=np.mean(t)
t_std=np.std(t,ddof=1)
normalize_t=[]
for j in t:
    normalize_t.append((j-t_mean)/t_std)

normalize_process=[]
process_mean=np.mean(process)
process_std=np.std(process,ddof=1)
for j in process:
    normalize_process.append((j-process_mean)/process_std)

normalize_port=[]
port_mean=np.mean(port)
port_std=np.std(port,ddof=1)
for j in port:
    normalize_port.append((j-port_mean)/port_std)

normalize_thread=[]
thread_mean=np.mean(thread)
thread_std=np.std(thread,ddof=1)
for j in thread:
    normalize_thread.append((j-thread_mean)/thread_std)

#从四个列表中整合出来新的value列表
with open("normalize_value.log","a+")as nv:
    for i in range(len(normalize_t)):
        writeline=str(normalize_t[i])+" "+str(normalize_process[i])+" "+str(normalize_port[i])+" "+str(normalize_thread[i])+"\n"
        nv.write(writeline)

