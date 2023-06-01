from setuptools import setup

setup(
    name='python-url-shortener',
    version='1.0.0',
    author='Morgan Collens',
    description='A simple project designed to help learn the fundamentals of python. Built using both Python and Flask, this service is designed to allow a user to shorten a url and access the original URL via the shortened version.',
    packages=['python-url-shortener'],
    install_requires=[
        'Flask',
        'mysql-connector-python',
        'python-dotenv',
        'validators',
        'redis'
    ],
)