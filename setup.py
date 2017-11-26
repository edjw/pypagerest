from setuptools import setup

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
    python_requires=['>=3.4'],
    install_requires=['requests>2.18.0'],
    zip_safe=False
)

# # from sys import version_info

# try:
#     from setuptools import setup
# except ImportError:
#     from distutils.core import setup

# # if version_info < (3, 4):
# #     raise RuntimeError("This package requres Python 3.4+")

# setup(
#     name='pypagerest',
#     description='A Python wrapper for Page.REST',
#     long_description='A Python wrapper for Page.REST – an HTTP API you can use to extract content from any web page as JSON',
#     keywords='Page.REST scraping api Python wrapper async asynchronous',
#     url='https://github.com/edjw/pypagerest',
#     author='Ed Johnson-Williams',
#     author_email='edjohnsonwilliams@gmail.com',
#     version='0.2',
#     license='MIT',
#     packages=['pypagerest'],
#     zip_safe=False,
#     python_requires=['>=3.4'],
#     install_requires=['requests>=2.17.0']
# )
