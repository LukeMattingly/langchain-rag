from queue import Queue
from threading import Thread
from app.chat.callbacks.stream import StreamingHandler
from flask import current_app as app

class StreamableChain:
    def stream(self, input):
        queue = Queue()
        handler = StreamingHandler(queue)

        def task(app_context):
            app_context.push()
            self(input, callbacks=[handler]) #running the chain, using it's own handler

        Thread(target=task, args=[app.app_context()]).start()
        
        while True:
            token = queue.get()
            if token is None:
                break
            yield token