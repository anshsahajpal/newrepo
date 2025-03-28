import os


USER_API_URL = os.getenv("USER_API_URL")
def check_config():
    if not USER_API_URL:
        raise Exception("USER API URL NOT DEFINED")
