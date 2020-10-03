"""
    Este script verifica se:
    → Estão instalados os pré requisitos
    → Arquivos de configuração estão intactos
    Ele também:
    → Realiza a instalação e reparo de componentes necessários
"""

from platform import system
from shutil import which
from os import system as terminal
from os.path import expanduser, isdir, isfile
from os import makedirs
from json import load, dump
from datetime import datetime
from math import floor
from socket import create_connection

def get_pkg_mng():
    # TODO: Adicionar mais gerenciadores de pacotes
    if(which("apt")): return "apt"
    if(which("dnf")): return "dnf"
    if(which("pacman")): return "pacman"

def linux_install(pkg_mng, pkg): terminal(f"sudo {pkg_mng} -y install {pkg}")
def linux_has_emojione(): return terminal('fc-list | grep -q emojione') >= 1
def custom_timestamp(): return floor(datetime.timestamp(datetime.now())/2592000)
def read_json(file):
    tmp = {}
    with open(file, "r") as read_file:
        tmp = load(read_file)
    return tmp
def comparate_json(data, file): return read_json(file) == data


cfg_path = expanduser("~")+"/.gyt"
os_type = system()
last_check = { 'is': custom_timestamp() } # quando for diferente atualizar

# instalando dependências
if os_type == "Linux":
    pkg_mng = get_pkg_mng()
    if not which("git"): linux_install(pkg_mng, "git")
    if  linux_has_emojione(): linux_install(pkg_mng, "fonts-emojione")

# TODO: Criar depois versão windows
if os_type == "Windows": pass

#Checagem da integridade dos arquivos de configuração
cache_path = cfg_path+"/cache"
comparator_path = cfg_path+"/comparator"
if not isdir(cfg_path): makedirs(cfg_path)
if not isdir(cache_path): makedirs(cache_path)
if not isdir(comparator_path): makedirs(comparator_path)

#atualizando arquivos
check_file = cfg_path+"/last_check.json"
if not isfile(check_file): #identificando arquivos vazios
    with open(check_file, "w") as file:
        dump(last_check, file)
else:
    if not comparate_json(last_check, check_file):
        pass #atualização mensal

data_path = {
    "ignores": cache_path  + "/ignores.json",
    "licenses":cache_path  + "/licenses.json",
    "emoji": cache_path  + "emoji.json"
}

def is_connected():
    try:
        create_connection(('1.1.1.1', 53))
        return 1
    except OSError: return 0
