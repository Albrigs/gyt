#!/usr/bin/env python3
# import scripts.os_checker
from __future__ import print_function, unicode_literals
from PyInquirer import prompt
from scripts.commiter import commit as exec_commit
import click
from scripts.licenser import add_license, list_licenses
from scripts.ignorer import  add_ignores

@click.command()
@click.option('-c','--commit', is_flag=True,
help='')
@click.option('-ca','--commitall', is_flag=True,
help='')
@click.option('-l','--license', is_flag=True,
help='')
@click.option('-i','--gitignores', is_flag=True,
help='')

def main(commit, commitall, license, gitignores, list):
    flags = commit + commitall + license + gitignores + list
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
        if license and not list: add_license()
        if gitignores and not list: add_ignores()

if __name__ == '__main__':
    main()
