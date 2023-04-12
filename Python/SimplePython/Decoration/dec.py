"""
Декоратор который ближе к функции выполняется первый 
"""

def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Position arguments:', args)
        print('Keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result 
    return new_function


def squart_it(func):
    def new_func(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result
    return new_func


@document_it    #2
@squart_it      #1
def add_ints_ds(a, b):
    return a + b 


@squart_it      #2
@document_it    #1 
def add_ints_sd(a, b):
    return a + b 


if __name__ == '__main__':
    
    print(add_ints_ds(3,5))
    print(add_ints_sd(3,5))
