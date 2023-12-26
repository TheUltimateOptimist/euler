import time
import sys

def timing(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()*1000
        result = func(*args, **kwargs)
        end_time = time.time()*1000
        elapsed_time = end_time - start_time
        print(f"{func.__name__} took {elapsed_time} ms")
        return result
    return wrapper

def read(name: str) -> str:
    folder = sys.argv[0].split("/")[-2]
    with open(f"{folder}/{name}", mode="r", encoding="ascii") as file:
        return file.read()