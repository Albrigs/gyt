from __future__ import print_function, unicode_literals
from PyInquirer import prompt
from .wgetter import get_ignores_ref

def select_langs(selected=0):
    """
        Seleciona linguagens que irão ser utilizadas nos gitignores.
    """
    selected = [e[0] for e in selected]
    ignores_list = get_ignores_ref()
    if selected:
        choices = [{'name': e, 'checked': e in selected} for e in get_ignores_ref()]
    else:
        choices = [{'name': e} for e in get_ignores_ref()]
    pass
    questions = [
        {
            'type': 'checkbox',
            'message': 'Select your languages for your default ignores.',
            'name': 'languages',
            'choices': choices,
            'validate': lambda answer: 'You must choose at least one option.' \
                if len(answer) == 0 else True
        }
    ]
    languages = prompt(questions)['languages']
    res = {}
    for e in languages:
        res[e] = ignores_list[e]
    return res
