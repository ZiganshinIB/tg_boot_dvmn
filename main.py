from environs import Env
import json

from api_dvmn import Devman

env = Env()
env.read_env()

if __name__ == '__main__':
    dvmn = Devman(env.str('DEVMAN_TOKEN'))
    while True:
        print(json.dumps(dvmn.get_reviews(), indent=4, ensure_ascii=False))
        print(json.dumps(dvmn.get_long_polling(), indent=4, ensure_ascii=False))
