from datetime import datetime


def log_file(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        log = f'{datetime.now()} running "{function.__name__}" with arguments {args},{kwargs} result is {result} \n'
        with open('logfile.txt', 'a', encoding='utf-8') as logfile:
            logfile.write(log)
        return result

    return wrapper


def log_file_with_path(path):
    def new_log_file(function):
        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs)
            log = f'{datetime.now()} running "{function.__name__}" with arguments {args},{kwargs} result is {result} \n'
            with open(path, 'a', encoding='utf-8') as logfile:
                logfile.write(log)
            return result
        return wrapper
    return new_log_file
