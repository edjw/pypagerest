from sys import version_info
from setuptools import setup

if version_info < (3, 5):
    raise RuntimeError("This package requres Python 3.5+")

setup(
    name='pypagerest',
    description='A Python wrapper for Page.REST',
    long_description='A Python wrapper for Page.REST – an HTTP API you can use to extract content from any web page as JSON',
    keywords='Page.REST scraping api Python wrapper',
    url='https://github.com/edjw/pypagerest',
    author='Ed Johnson-Williams',
    author_email='edjohnsonwilliams@gmail.com',
    version='0.2',
    license='MIT',
    packages=['pypagerest'],
    python_requires='~=3.5',
    install_requires=['requests>2.18.0'],
    zip_safe=False
)
