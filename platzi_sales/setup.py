from setuptools import setup
# how to call the command line
setup(
    name='pv',
    version='0.1',
    py_modules=['pv'],
    intall_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        pv=pv:cli
    ''',
)
