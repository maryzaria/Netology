import requests


def request():
    url = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json"
    response = requests.get(url)
    data = response.json()
    res = {}
    for superhero in data:
        name = superhero['name']
        if name in ('Hulk', 'Captain America', 'Thanos'):
            res[name] = superhero['powerstats']['intelligence']
    return max(res.items(), key=lambda x: x[1])[0]


if __name__ == '__main__':
    print(f'Самый умный супергерой: {request()}')
