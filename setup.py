from setuptools import setup

setup(
    name='acme',
    version='0.1',
    py_modules=['acme'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        acme=acme:cli
    ''',
)