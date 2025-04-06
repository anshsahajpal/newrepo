from uuid import UUID

import redis
import inspect


class RedisConnectionManager:
    def __init__(self, host='localhost', port=6379):
        caller = inspect.stack()[1].filename
        print(f"Connecting to Redis service at host: {host}, port: {port} from module: {caller}")
        self.redis = redis.StrictRedis(host=host, port=port, decode_responses=True)

    def store_user_connection(self, user_id: UUID, server_id: str):
        self.redis.hset("ws:connections", user_id, server_id)

    def delete_user_connection(self, user_id: UUID):
        self.redis.hdel("ws:connections", user_id)

    def get_user_connection(self, user_id: UUID):
        connection = self.redis.hget("ws:connections", user_id)
        if connection:
            return connection
        else:
            return None
