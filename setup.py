from setuptools import setup

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
    version='0.1',
    license='MIT',
    packages=['pypagerest'],
)