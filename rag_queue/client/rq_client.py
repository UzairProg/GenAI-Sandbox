from rq import Queue
from redis import Redis

queue = Queue(connection=Redis(
    host='localhost', port=6379
    ))

# queue.enqueue() # takes (fnc, *args)