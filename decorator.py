import datetime


def log_file(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        log = f'{datetime.datetime.now()} running "{function.__name__}" with arguments {args},{kwargs} result is {result} \n'
        with open('logfile.txt', 'a', encoding='utf-8') as logfile:
            logfile.write(log)
        return result

    return wrapper
