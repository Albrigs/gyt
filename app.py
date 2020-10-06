#!/usr/bin/env python3
# import scripts.os_checker
from __future__ import print_function, unicode_literals
from PyInquirer import prompt
from scripts.commiter import commit as exec_commit
import click
from scripts.licenser import add_license
from scripts.ignorer import  add_ignores

import scripts.os_checker
del scripts.os_checker

@click.command()
@click.option('-c','--commit', is_flag=True,
help='Commit with git.')
@click.option('-ca','--commitall', is_flag=True,
help='Commit and track all files.')
@click.option('-l','--license', is_flag=True,
help='Add a license.')
@click.option('-i','--gitignores', is_flag=True,
help='Add or expand a .gitignore.')

def main(commit, commitall, license, gitignores):
    flags = commit + commitall + license + gitignores
    if flags > 1:
        return print("JUST ONE FLAG PLOX!")

    if flags == 0:
        questions = [
            {
                'type': 'list',
                'name': 'action',
                'message': 'What you wanna do?',
                'choices': [
                    "Commit",
                    "Add * and Commit",
                    "Add GitIgnore",
                    "Add License",
                ]
            }
        ]

        #Criando estrutura de controle booleano
        answers = prompt(questions)
        commit = answers['action'] == "Commit"
        commitall = answers['action'] == "Add * and Commit"
        license = answers['action'] == "Add License"
        gitignores = answers['action'] == "Add GitIgnore"

        if commit: exec_commit()
        if commitall: exec_commit(True)
        if license: add_license()
        if gitignores: add_ignores()

if __name__ == '__main__':
    main()
