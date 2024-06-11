from celery import Celery
from time import sleep
from random import randint

app = Celery('task', broker="amqp://guest@localhost")

@app.task
def hello(nome:str):
    sleep(5)
    if randint(1, 4) == 1:
        raise Exeption("Deu ruim")
    return "hello {}".format(nome)

