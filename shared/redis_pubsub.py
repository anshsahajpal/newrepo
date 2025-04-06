import json
import threading
import redis
import asyncio
import inspect

class RedisPubsub:
    def __init__(self, host='localhost', port=6379, channel='default'):
        self.redis = redis.StrictRedis(host=host, port=port, decode_responses=True)
        self.channel = channel
        caller = inspect.stack()[1].filename
        print(f"Connecting to Redis pubsub service at host: {host}, port: {port} from module: {caller}")
        

    def publish(self, message):
        self.redis.publish(self.channel, json.dumps(message))

    def subscribe(self, callback):
        if hasattr(self, 'subscribed') and self.subscribed:
            return
        self.subscribed = True
        loop = asyncio.get_event_loop()
        def run():
            pubsub = self.redis.pubsub()
            pubsub.subscribe(self.channel)
            for message in pubsub.listen():
                if message['type'] == 'message':
                    data = message['data']
                    asyncio.run_coroutine_threadsafe(callback(data), loop)

        # Start in a background thread
        threading.Thread(target=run, daemon=True).start()