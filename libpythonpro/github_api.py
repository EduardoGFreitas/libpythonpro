import requests


def buscar_avatar(avatar):
    """
        Busca o avatar de um usuário no github
        :param usuario: str com o nome de usuário no github
        :return:str com o link  do avatar
    """
    #url  = 'https://api.github.com/users/{}'.format(avatar)
    url = f'https://api.github.com/users/{avatar}'
    resp = requests.get(url)

    return resp.json()['avatar_url']

if __name__  == '__main__':
    print(buscar_avatar('renzon'))