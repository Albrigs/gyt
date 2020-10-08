from __future__ import print_function, unicode_literals
from PyInquirer import prompt

from os.path import isfile
from .wgetter import get_ignore
from .os_checker import db


def add_ignores():
    res = ''
    if isfile('.gitignore'):
        file = open('.gitignore', 'r')
        res += file.read()
        file.close()

    ignores_list = {}
    for e in db.table_content('langs'):
        ignores_list[e[0]] = e[1]

    choices = [{'name': e} for e in ignores_list.keys()]

    questions = [
        {
            'type': 'checkbox',
            'message': 'Select your ignore',
            'name': 'languages',
            'choices': choices,
            'validate': lambda answer: 'You must choose at least one option.' \
                if len(answer) == 0 else True
        }
    ]

    languages = prompt(questions)['languages']
    links = [ignores_list[e] for e in languages]

    for link in links:
        tmp = get_ignore(link)
        res += "\n\n#-----------------------------------\n\n" + ''.join(tmp.decode("utf-8"))

    file = open('.gitignore', 'w')
    file.write(res)
    file.close()
