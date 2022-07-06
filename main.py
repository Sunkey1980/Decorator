from decorator import log_file, log_file_with_path


@log_file
def first_func(*args):
    res = 0
    for arg in args:
        res += arg
    return res


@log_file_with_path('logs/logfile.txt')
def second_func(*args):
    res = 1
    for arg in args:
        res *= arg
    return res


if __name__ == '__main__':
    first_func(1, 6, 3, 8, 45)
    second_func(4, 2, 8)
