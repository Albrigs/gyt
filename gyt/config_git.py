from os import popen
from os.path import isfile
# popen vazio retorna ''


def _hasnt_git_cfg(manually, git_cfg):
	"""
	Se uma configuração no git ainda não existir irá cobrar que seja feita.
	"""
	if (not popen(git_cfg).read()) or manually:
		txt = git_cfg.split('.')[-1]
		tmp = input(f"What is your {txt} for git?")
		popen(f"{git_cfg} {tmp}")
		print(f"{txt} configured as {tmp}")
		return 0
	else:
		return 1

def config_git(manually = 0):
	if not isfile('~/.ssh/id_rsa.pub'):
		popen("ssh-keygen -f ~/.ssh/id_rsa -P ''")

	pub_key = popen('cat ~/.ssh/id_rsa.pub').read()

	git_name = 'git config --global user.name'
	git_email = 'git config --global user.email'
	git_editor = 'git config --global core.editor'

	git_name = _hasnt_git_cfg(manually, git_name)
	git_email = _hasnt_git_cfg(manually, git_email)
	git_editor = _hasnt_git_cfg(manually, git_editor)

	if not git_name * git_email * git_editor + manually:
		input(f"This is your pubkey, copy and paste in github settings, ok?\n\n\n{pub_key}")