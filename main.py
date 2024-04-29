import requests

if __name__ == '__main__':
    response = requests.get('https://api.github.com/events')
    print(response)