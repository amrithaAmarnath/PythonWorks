# Python threads
# thread is an object
# simple sleep program
# from time import sleep
# def task():
#     # block for a moment
#     sleep(3) #wait for 3ms
#     #display a message
#     print('this is from another thread')
# #task()
#
# from threading import Thread
# #creating a thread
# thread = Thread(target=task)
# #Next, we can create an instance of the threading. Tread class and specify
# #our function name as the "target" argument in the constructor.
# #run the thread
# thread.start()

# #The start() function doesnot block, it returns immediately
#
# from time import sleep
# from threading import Thread
# def task(sleep_time,msg):
#     # block for a moment
#     sleep(sleep_time) #wait for 3ms
#     #display a message
#     print(msg)
# #task()
#
#
# #creating a thread
# thread = Thread(target=task, args=(1.5,'this is from another thread'))
# #Next, we can create an instance of the threading. Tread class and specify
# #our function name as the "target" argument in the constructor.
# #run the thread
# thread.start()
# thread.join()

import time
import threading


def cal_sqre(num):
    print("Calculate square of a given number")
    for n in num:
        time.sleep(0.3)
        print('square is:', n * n)


def cal_cube(num):
    print("Calculate cube of a given number")
    for n in num:
        time.sleep(0.3)
        print('cube is:', n * n * n)


arr = [4, 5, 6, 7, 2]
t1 = time.time() #get total time to execute the functions
th1 = threading.Thread(target=cal_sqre,args=(arr,))
th2 = threading.Thread(target=cal_cube,args=(arr,))
th1.start()
th2.start()
th1.join()
th2.join()
print('total time taken by threads : ',time.time() - t1)

