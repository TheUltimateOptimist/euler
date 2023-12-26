import time

def timing(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()*1000
        result = func(*args, **kwargs)
        end_time = time.time()*1000
        elapsed_time = end_time - start_time
        print(f"{func.__name__} took {elapsed_time} ms")
        return result
    return wrapper