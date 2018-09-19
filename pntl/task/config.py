
import os


task_runner = None

try:

    import redis
    from huey import RedisHuey

    task_runner = RedisHuey('pntl_task', host=os.getenv('REDISH_HOST', 'redis://127.0.0.1:6379/1'))

except ImportError:

    from huey.contrib.sqlitedb import SqliteHuey
    task_runner = SqliteHuey('pntl_task.db')
