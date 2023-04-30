import threading, queue
import time 


def washer(dishes, dish_queue):
    for dish in dishes:
        print('Washing', dish)
        # time.sleep(5)
        dish_queue.put(dish)

def dryer(dish_queue):
    while True:
        dish = dish_queue.get() # получаем из очереди 
        print('Drying', dish)
        time.sleep(10)
        dish_queue.task_done()


if __name__ == '__main__':
    dish_queue = queue.Queue()
    for i in range(2): # cоздаем 2 потока 
        dryer_thread = threading.Thread(target=dryer, args=(dish_queue,))
        dryer_thread.start() # запускаем потоки
    
    dishes = ['salad', 'bread', 'entree', 'dessert', 'help'] # задачи
    washer(dishes, dish_queue) # заносим в очередь
    dish_queue.join()  # блокируем пока не обработаются все задачи 
    