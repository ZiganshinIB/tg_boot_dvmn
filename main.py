import time

import json


from environs import Env
from requests import exceptions

from api_dvmn import Devman

env = Env()
env.read_env()

if __name__ == '__main__':
    dvmn = Devman(env.str('DEVMAN_TOKEN'))
    while True:
        try:
            print(json.dumps(dvmn.get_reviews(), indent=4, ensure_ascii=False))
            print(json.dumps(dvmn.get_long_polling(), indent=4, ensure_ascii=False))
            time.sleep(5)
        except exceptions.ReadTimeout as e:
            print(e)
        except exceptions.ConnectionError as e:
            print(e)
            print('Ошибка соединения. Повторная попытка через 5 секунд')
            time.sleep(5)


