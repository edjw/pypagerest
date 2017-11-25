from sys import version_info
from setuptools import setup

if version_info < (3, 4):
    raise RuntimeError("This package requres Python 3.4+")

with open('README.md', 'r', encoding='utf-8') as readme:
    long_description = '\n' + readme.read()

setup(
    name='pypagerest',
    description='A Python wrapper for Page.REST',
    long_description=long_description,
    keywords='Page.REST scraping api Python wrapper',
    url='https://github.com/edjw/pypagerest',
    author='Ed Johnson-Williams',
    author_email='edjohnsonwilliams@gmail.com',
    version='0.2',
    license='MIT',
    packages=['pypagerest'],
    python_requires=['>=3.4'],
    install_requires=['requests>2.18'],
    zip_safe=False
)
