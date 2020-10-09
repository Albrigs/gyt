import setuptools

#with open("README.md", "r") as fh:
#    long_description = fh.read()

setuptools.setup(
    name="gyt",
    version="0.0.2",
    author="Natan 'Albrigs' Fernandes dos Santos",
    author_email="natanfernandessantos@protonmail.com",
    description="",
    #long_description=long_description,
    #long_description_content_type="text/markdown",
    url="https://github.com/Albrigs/gyt",
    packages=['gyt'],
    classifiers=[

    ],
    install_requires=['click', 'emojis', 'requests', 'PyInquirer'],
    python_requires='>=3.6',
    entry_points = {
        'console_scripts': [
            'gyt = gyt.__main__:main'
        ]
    }
)
