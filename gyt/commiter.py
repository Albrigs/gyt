from __future__ import print_function, unicode_literals
from PyInquirer import prompt

from pprint import pprint
from .default_paterns import targets
from os import system


def emoji_questions_gen(emoji_set, msg):

    choices_label = [e.label for e in emoji_set]
    choices_emoji = [e.emoji for e in emoji_set]
    choices_text = [f'{e} | {choices_label[i]}' for i, e in enumerate(choices_emoji)]

    questions = [
        {
            'type': 'list',
            'name': 'res',
            'message': msg,
            'choices': choices_text,
             'filter': lambda val: val.split("| ")[1]
        }
    ]

    aw = prompt(questions)
    selected = [e for e in emoji_set if e.label == aw['res']][0]
    return selected

def commit(stage_all=False):
    emoji1 = emoji_questions_gen(targets, 'What you had changed?')
    emoji2 = emoji_questions_gen(emoji1.actions, 'How you had changed it?')

    questions = [
        {
            'type': 'input',
            'name': 'title',
            'message': 'Commit title:',
        },
        {
            'type': 'input',
            'name': 'body',
            'message': 'Commit body:',
        },
    ]
    title, body = prompt(questions).values()

    print(f'{emoji1.emoji}{emoji2.emoji} { title }\n{ body }')

    all = stage_all*"-a"
    system(f"git commit {all} -m\"{emoji1.emoji_name}{emoji2.emoji_name}{title}\" -m \"{body}\" ")
