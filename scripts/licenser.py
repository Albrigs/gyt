from __future__ import print_function, unicode_literals
from PyInquirer import prompt
from wgetter import get_licenses_ref, get_license
from pprint import pprint

def list_licenses():
    get_licenses_ref()


def add_license():
    lic_list = get_licenses_ref()
    questions = [
        {
            'type': 'list',
            'name': 'res',
            'message': "What license you want?",
            'choices': lic_list.keys(),
        }
    ]

    license = prompt(questions)['res']

    body, permissions = get_license(*lic_list[license])

    questions = [
    {
        'type': 'confirm',
        'message': f'This licence had this permissions: {permissions} \n\nContinue?',
        'name': 'continue',
        'default': True,
    }
    ]

    confirm = prompt(questions)['continue']

    if confirm:
        file = open("LICENSE.md", "w")
        file.write(body)
        file.close()

add_license()
