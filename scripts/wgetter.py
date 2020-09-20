from pprint import pprint
from requests import get
from base64 import b64decode

b_url_ignore = "https://api.github.com/repos/github/gitignore/"

def get_ignores_ref():
    """
    Pega os nomes e url dos ignores principais do git
    """
    # TODO: Adicionar a busca dentro das pastas do diretório

    tmp_ignore_data = get(b_url_ignore+"git/trees/master").json()['tree']

    ignore_paths = []
    for e in tmp_ignore_data:
        if e["path"].endswith("ignore"): ignore_paths.append(e["path"])

    ignore_data_from_git = {}
    for e in ignore_paths:
        ignore_data_from_git[e.split('.')[0].lower()] = b_url_ignore+"contents/"+e

    return ignore_data_from_git

def get_ignore(target_url):
    """Busca um ignore no repositório e retorna seu texto"""
    url = get(target_url).json()["git_url"]
    return b64decode(get(url).json()["content"])


def get_licenses_ref():
    "Pega urls das licensas e as retornas indexadas em um array"
    res = {}
    tmp = get("https://api.github.com/licenses").json()

    for e in tmp: res[e["key"]] = [e["url"]]

    return res

def get_license(target_url):
    """Busca uma licensa na api e retorna seu texto"""
    tmp = get(target_url).json()
    return tmp['body'], tmp["permissions"]

def get_emojis():
     return = get("https://api.github.com/emojis").json().keys()
