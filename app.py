#!/usr/bin/env python3
# import scripts.os_checker
from __future__ import print_function, unicode_literals
from pprint import pprint
from PyInquirer import prompt
import click


@click.command()
@click.option('-c','--commit', is_flag=True,
help='')
@click.option('-ca','--commitall', is_flag=True,
help='')
@click.option('-l','--license', is_flag=True,
help='')
@click.option('-i','--gitignores', is_flag=True,
help='')
@click.option('--list', is_flag=True,
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
                    "List GitIgnore"
                    "Add License",
                    "List Licenses",
                ]
            }
        ]

        #Criando estrutura de controle booleano
        answers = prompt(questions)
        commit = answers['action'] == "Commit"
        commitall = answers['action'] == "Add * and Commit"
        license = answers['action'] == "Add License" or answers['action'] == "List Licenses"
        gitignores = answers['action'] == "Add GitIgnore" or answers['action'] == "List GitIgnore"
        list = answers['action'] == "List Licenses" or answers['action'] == "List GitIgnore"

        if commit: pass
        if commitall: pass
        if license and not list: pass
        if license and list: pass
        if gitignores and not list: pass
        if gitignores and list: pass

if __name__ == '__main__':
    main()
