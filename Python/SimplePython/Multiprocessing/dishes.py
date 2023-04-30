import multiprocessing as mp
from time import sleep
from random import randint


def washer(dishes, output):
    for dish in dishes:
        print('Washing', dish, 'dish')
        output.put(dish)
        sleep(randint(0,10))
        


def dryer(input):
    while True:
        dish = input.get()
        print('Drying', dish,'dish')
        # sleep(randint(0,10)) 
        input.task_done()

if __name__ == '__main__':
    dish_queue = mp.JoinableQueue() #создаем очередь
    dryer_proc = mp.Process(target=dryer, args=(dish_queue,)) #создаем процесс 

    dryer_proc.daemon = True #убивает процесс когда заканчивается очередь
    dryer_proc.start() #запускаем поток на получение задачи

    dishes = ['salad', 'bread', 'entree', 'dessert']
    washer(dishes, dish_queue) # заносим в очередь 
    dish_queue.join() # объединяем очередь 


