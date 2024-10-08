from celery import Celery

from config import REDIS_HOST

# celery config
CELERY_BROKER_URL = f'redis://{REDIS_HOST}/0'
CELERY_RESULT_BACKEND = f'redis://{REDIS_HOST}/0'


# initialize celery app
def make_celery(app):
    celery = Celery(app.import_name, broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)
    celery.conf.update(app.config)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery