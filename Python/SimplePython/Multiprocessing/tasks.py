from invoke import task

"""
 с помощью команды >invoke mytime получаем дату в консоле
 так же есть похожие пакеты click, doit, sh, delegator, pypl
"""


@task
def mytime(ctx):
    import time
    now = time.time()
    time_str = time.asctime(time.localtime(now))
    print("local time is", time_str)
