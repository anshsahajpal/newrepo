import os
import random


server_id = random.randint(1, 1000000)
redis_host = os.getenv("REDIS_HOST", "localhost")
redis_port = os.getenv("REDIS_PORT", 6379)