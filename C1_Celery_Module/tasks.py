import time
from celery import Celery

# define a celery module
app = Celery('tasks', backend='mongodb://localhost:27017/celery', broker='redis://localhost:6379/0')

# function to be performed with celery
# define the task with task decorator:
# you can give in your own name or celery will pick one for you. 
@app.task(name='tasks.add')
def add(x, y):
    total = x + y
    print('{} + {} = {}'.format(x, y, total))
    time.sleep(10)
    return total

