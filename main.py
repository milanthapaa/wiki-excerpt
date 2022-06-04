import requests


def random_wiki():
    userinput = input("Search excerpt in wikipedia: ")
    request = requests.get(
        f'https://en.wikipedia.org/api/rest_v1/page/summary/{userinput}')
    status_code = 200



if __name__ == "__main__":
    random_wiki()
