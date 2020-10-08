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
from math import floor
from db_handler import DBHandler

os_type = system()

def get_pkg_mng():
    # TODO: Adicionar mais gerenciadores de pacotes
    if(which("apt")): return "apt"
    if(which("dnf")): return "dnf"
    if(which("pacman")): return "pacman"

def linux_install(pkg_mng, pkg): terminal(f"sudo {pkg_mng} -y install {pkg}")
def linux_has_emojione(): return terminal('fc-list | grep -q emojione') >= 1

# instalando dependências
if os_type == "Linux":
    pkg_mng = get_pkg_mng()
    if not which("git"): linux_install(pkg_mng, "git")
    if  linux_has_emojione(): linux_install(pkg_mng, "fonts-emojione")

# TODO: Criar depois versão windows
if os_type == "Windows": pass

db = DBHandler()
