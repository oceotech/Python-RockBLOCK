
from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='rockblock',
    version='0.0.0',

    description='RockBLOCK modem driver for use of the Iridium SBD service',
    long_description=long_description,

    url='https://github.com/oceotech/Python-RockBLOCK',

    author='Andrew Carter',
    author_email='andrewcarter1992@gmail.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='rockblock 9603 iridium sbd',

    packages=['rockblock'],

    include_package_data=True,

    install_requires=['pyserial'],
)
