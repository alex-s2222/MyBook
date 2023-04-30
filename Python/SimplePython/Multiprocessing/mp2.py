from multiprocessing import Process
import os 
import time 

"""
Выводит 10 раз "Honk" (так как стоит sleep(10)) после этого убивает процесс
"""


def whoami(what):
    print("Process %s says %s" %(os.getpid(), what))


def loopy(name):
    whoami(name)
    start = 1
    end = 1000
    for num in range(start, end):
        print("\tNumber %s of %s. Honk!" %(num, end))
        time.sleep(1)


if __name__ == '__main__':
    whoami("I'm the main program")
    p = Process(target=loopy, args=("loopy",))
    p.start()
    print('\tHello')
    time.sleep(10)
    print('Hello2')
    p.terminate()