import requests


def random_wiki():
    userinput = input("Search excerpt in wikipedia: ")
    request = requests.get(
        f'https://en.wikipedia.org/api/rest_v1/page/summary/{userinput}')
    status_code = 200
    data = request.json()

    if request.status_code == status_code:
        with open(f'{userinput}.txt', 'w') as f:
            f.write(data['extract'])
    else:
        return "Couldn't retrieve the data, request error"


if __name__ == "__main__":
    random_wiki()
