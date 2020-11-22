import queue #队列对象模块
import threading
import time
import random

q = queue.Queue(5) #创建一个管道对象


#银行业务窗口

def worker():
    while True:
        task = q.get() #从队列对象中取值，计数器加1
        print(f'\n第{task}个顾客到窗口办理业务。')
        t=random.randint(3,6)
        time.sleep(t)
        q.task_done() #给队列对象反馈任务完成，计数器减1
        print(f'\n第{task}个顾客业务办理完成！')
  

t = threading.Thread(target=worker) #创建线程对象
t.start() #启动线程对象


#顾客

for i in range(0,13):
    print(f'\n第{i}个顾客取号。')
    time.sleep(random.randint(2,4))
    q.put(i)

q.join()
print(f'\n所有顾客的业务办理完成!')
