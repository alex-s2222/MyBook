from multiprocessing import Process
import os 
from random import randint
import time

"""
Ждет пока все выполниться после этого выводится ответ  
Перед этим выводится hello
"""

def whoami(what):
    print("Process %s says %s" %(os.getpid(), what))
    time.sleep(randint(0,10))



if __name__ == '__main__':
    whoami("I'm the main program")
    for i in range(5):
        p = Process(target=whoami, args=(i,))
        p.start()
    print('Hello')