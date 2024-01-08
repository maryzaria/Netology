import datetime
import os
import logging
from logging.handlers import RotatingFileHandler
from functools import wraps


# _________________________
# task 1

def logger_v1(old_function):
    path = 'main.log'

    @wraps(old_function)
    def new_function(*args, **kwargs):
        result = old_function(*args, **kwargs)

        with open(path, 'a') as log_file:
            log_file.write(f'''
            {datetime.datetime.now()}
            Вызвана функция {old_function.__name__}
            c аргументами {args} и {kwargs} 
            Результат: {result}
            ______________________''')

        return result

    return new_function


def logger_v2(old_function):
    path = 'main.log'
    __logger = logging.getLogger(path)
    __logger.setLevel(logging.DEBUG)
    handler = RotatingFileHandler(path, backupCount=10, maxBytes=1000000)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    __logger.addHandler(handler)

    @wraps(old_function)
    def new_function(*args, **kwargs):
        result = old_function(*args, **kwargs)

        __logger.debug(
            f'Вызвана функция {old_function.__name__} c аргументами {args} и {kwargs} Результат: {result}'
        )

        return result

    return new_function


def logger_v3(path):
    def _logger(old_function):
        @wraps(old_function)
        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)

            with open(path, 'a') as log_file:
                log_file.write(f'''
                {datetime.datetime.now()}
                Вызвана функция {old_function.__name__}
                c аргументами {args} и {kwargs} 
                Результат: {result}
                ______________________''')

            return result

        return new_function

    return _logger


def logger_v4(path):
    __logger = logging.getLogger(path)
    __logger.setLevel(logging.DEBUG)
    handler = RotatingFileHandler(path, backupCount=10, maxBytes=1000000)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    __logger.addHandler(handler)

    def _logger(old_function):
        @wraps(old_function)
        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)

            __logger.debug(
                f'Вызвана функция {old_function.__name__} c аргументами {args} и {kwargs} Результат: {result}'
            )

            return result

        return new_function

    return _logger


def test():
    paths = (
        'main.log', 'main.log',
        'log_1.log', 'log_2.log', 'log_3.log',
        'log_1.log', 'log_2.log', 'log_3.log')

    for path in paths:
        if os.path.exists(path):
            os.remove(path)
    loggers = (
        logger_v1, logger_v2,
        logger_v3('log_1.log'), logger_v3('log_2.log'), logger_v3('log_3.log'),
        logger_v4('log_1.log'), logger_v4('log_2.log'), logger_v4('log_3.log')
    )

    for path, logger in zip(paths, loggers):
        @logger
        def summator(a, b=0):
            return a + b

        @logger
        def div(a, b):
            return a / b

        result = summator(2, 2)
        assert isinstance(result, int)
        assert result == 4, '2 + 2 = 4'
        result = div(6, 2)
        assert result == 3, '6 / 2 = 3'

        assert os.path.exists(path)

        summator(4.3, b=2.2)
        summator(a=0, b=0)

        with open(path) as log_file:
            log_file_content = log_file.read()

        assert 'summator' in log_file_content, 'должно записаться имя функции'
        for item in (4.3, 2.2, 6.5):
            assert str(item) in log_file_content, f'{item} должен быть записан в файл'


if __name__ == '__main__':
    test()