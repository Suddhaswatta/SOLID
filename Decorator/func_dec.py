import  time
def time_taken(func):
    """Takes in a function and modifies it"""
    def wrapper():
        start = time.time()
        result = func()
        end = time.time()
        print(f'{func.__name__} function took {int(end-start)} seconds')
        return result
    return wrapper

@time_taken
def my_func():
    time.sleep(1)
    return "Done "



my_func()
    