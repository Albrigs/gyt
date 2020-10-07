#!/usr/bin/env python3
from __future__ import print_function, unicode_literals
from PyInquirer import prompt
import scripts.os_checker
from scripts.commiter import commit as exec_commit
import click
from scripts.licenser import add_license
from scripts.ignorer import  add_ignores

@click.command()
@click.option('-c','--commit', is_flag=True,
help='Commit with git.')
@click.option('-ca','--commitall', is_flag=True,
help='Commit and track all files.')
@click.option('-l','--license', is_flag=True,
help='Add a license.')
@click.option('-i','--gitignores', is_flag=True,
help='Add or expand a .gitignore.')
@click.option('-e','--editgitignores', is_flag=True,
help='Change your ignores list.')


def main(commit, commitall, license, gitignores, editgitignores):
    flags = commit + commitall + license + gitignores + editgitignores
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
                    "Edit Default Ignores"
                ]
            }
        ]

        #Criando estrutura de controle booleano
        answers = prompt(questions)
        commit = answers['action'] == "Commit"
        commitall = answers['action'] == "Add * and Commit"
        license = answers['action'] == "Add License"
        gitignores = answers['action'] == "Add GitIgnore"
        editgitignores = answers['action'] == "Edit Default Ignores"

        if commit: exec_commit()
        if commitall: exec_commit(True)
        if license: add_license()
        if gitignores: add_ignores()
        if editgitignores: scripts.os_checker.db.config_langs()

if __name__ == '__main__':
    main()
