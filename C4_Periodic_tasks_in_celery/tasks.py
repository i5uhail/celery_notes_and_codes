import time
from celery import Celery

# for running periodic tasks
from celery.decorators import periodic_task

# for giving time differences
from datetime import timedelta

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


def backoff(attempts):
    """
    1, 2, 4, 8, 16 (attempts would be in this sequence.)
    """
    return 4 ** attempts

# A task being bound means the first argument to the task will always be the task instance (self), just like Python bound methods
"""
logger = get_task_logger(__name__)

@task(bind=True)
def add(self, x, y):
    logger.info(self.request.id)
"""
# max_tretires is an attribute within the decorator app.task that retries to run the function in case of an exception. 
# The soft time limit for this task. When not set the workers default is used.
@app.task(bind=True, max_retries=4, soft_time_limit=5)
def data_extractor(self):
    try:
        for i in range(1, 11):
            print('Crawling HTML DOM!')
            if i == 5:
                raise ValueError('Crawling Index Error')
    except Exception as exc:
        print('There was an exception lets rety after 5 seconds')
        # trigger the retry by invoking the task self object. 
        # Countdown usage http://docs.celeryproject.org/en/latest/userguide/tasks.html#using-a-custom-retry-delay
        raise self.retry(exc=exc, countdown=backoff(self.request.retries))

# periodic decorater gets picked up with the beats scheduler. 
# run every variable is a must and should be given in time delta or crintab. 
@periodic_task(run_every=timedelta(seconds=3), name="tasks.send_mail_from_queue")
def send_mail_from_queue():
    try:
        message_sent = "example.email"
        print("Email message successfully send, [{}]".format(message_sent))
    finally:
        print("release resources")