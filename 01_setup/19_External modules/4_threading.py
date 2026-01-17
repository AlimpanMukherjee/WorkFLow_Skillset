import time
import threading
def worker(num):
    print(f"Thread {num}:Starting")
    time.sleep(2) #simulate some work
    print(f"Thread {num}: Finishing")

threads=[]

for i in range(3):
    thread=threading.Thread(target=worker,args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    #wait for all threads to finish
    thread.join()
    print("threads completeed")

#we can use it for running parallely multiple functions but cannot execute cpu bound operations  parallely 