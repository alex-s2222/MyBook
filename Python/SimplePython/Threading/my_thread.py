import threading, queue
import time
from random import randint



def parsing(url:str):
    time.sleep(randint(0,5))
    return (url + 'hep')


def set_in_queue(urls, url_queue):
    for url in urls:
        print('Set', url)
        url_queue.put(url)


'''может быть создавать количесво work
     по количеству пользователей'''
def work(url_queue):
        # придумать тригер для что бы положить в бесконый цикл
        while True:
            url = url_queue.get()
            print(parsing(url))
            url_queue.task_done()
            

if __name__ == '__main__':
    url_queue = queue.Queue()
    for i in range(3):
            work_url = threading.Thread(target=work, args=(url_queue,))
            work_url.start()
    
    urls = ['1','2','3','4','5','6','7','8','9','11','12','13']
    
    for i in range(4):
        u = []
        for i in range(3):
            # создаем 3 url
            u.append(urls.pop(0))
        set_in_queue(u, url_queue) # вставляем url 
        url_queue.join() # блокирует поток
        time.sleep(5)
        print('Hello')
    

    #TODO придумать как реализовать в боте и как проверку сделать?

    
