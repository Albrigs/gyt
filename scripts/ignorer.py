from __future__ import print_function, unicode_literals
from PyInquirer import prompt

from os.path import isfile
from .wgetter import get_ignores_ref, get_ignore
from pprint import pprint

def add_ignores():
    res = ''
    if isfile('.gitignore'):
        file = open('.gitignore', 'r')
        res += file.read()
        file.close()

    ignores_list = get_ignores_ref()
    choices = [{'name': e} for e in get_ignores_ref()]

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
