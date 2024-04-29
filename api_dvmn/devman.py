import requests

class Devman:

    def __init__(self, token):
        self.token = token

    def get_request(self, url, params=None):
        """Получение данных из API"""
        response = requests.get(url, headers={'Authorization': f'Token {self.token}'}, params=params)
        response.raise_for_status()
        raw_data = response.json()
        if 'error' in raw_data:
            raise requests.exceptions.HTTPError(raw_data['error'])
        return raw_data

    def get_reviews(self,):
        """Получение списка проверок своих работ"""
        url = 'https://dvmn.org/api/user_reviews/'
        return self.get_request(url)

    def get_long_polling(self, timestamp=None):
        """Получение данных для Long Polling"""
        url = 'https://dvmn.org/api/long_polling/'
        if timestamp is None:
            params = {'timestamp': str(timestamp)}
            return self.get_request(url, params)
        return self.get_request(url)




