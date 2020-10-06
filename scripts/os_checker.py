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
from math import floor
from socket import create_connection
import sqlite3
from .languages_selector import select_langs

cfg_file  = expanduser("~")+"/.gyt.db"
os_type = system()

def get_pkg_mng():
    # TODO: Adicionar mais gerenciadores de pacotes
    if(which("apt")): return "apt"
    if(which("dnf")): return "dnf"
    if(which("pacman")): return "pacman"

def linux_install(pkg_mng, pkg): terminal(f"sudo {pkg_mng} -y install {pkg}")
def linux_has_emojione(): return terminal('fc-list | grep -q emojione') >= 1
def read_json(file):
    tmp = {}
    with open(file, "r") as read_file:
        tmp = load(read_file)
    return tmp
def comparate_json(data, file): return read_json(file) == data

def is_connected():
    try:
        create_connection(('1.1.1.1', 53))
        return 1
    except OSError: return 0

# instalando dependências
if os_type == "Linux":
    pkg_mng = get_pkg_mng()
    if not which("git"): linux_install(pkg_mng, "git")
    if  linux_has_emojione(): linux_install(pkg_mng, "fonts-emojione")

# TODO: Criar depois versão windows
if os_type == "Windows": pass

#criando base de dados
conn = sqlite3.connect(cfg_file)
cursor = conn.cursor()
exec_sql = cursor.execute
save_sql = conn.commit

def table_exists(name):
    """
    Retorna 1 ou 0 se a tabela existe ou não.
    """
    sql = f"SELECT name FROM sqlite_master WHERE type='table' AND name='{name}';"
    has_table = [e for e in exec_sql(sql)].__len__()
    return has_table

def table_content(name):
    """
    Retorna conteúdo de uma tabela ou 0 se estiver vazio
    """
    sql = f"SELECT * FROM {name};"
    content = [e for e in exec_sql(sql)]
    if not content.__len__(): return 0
    return content

#rotina de verificação inicial
if not table_exists('langs'):
    cursor.execute("""
        CREATE TABLE langs (
                lang TEXT NOT NULL,
                url TEXT NOT NULL
        );
    """)
    save_sql()

if not table_content('langs'):
    langs = select_langs()
    for key in langs:
        exec_sql(f"INSERT INTO langs VALUES ( '{key}', '{langs[key]}' )")
    save_sql()

selected_ignores = table_content('langs')
