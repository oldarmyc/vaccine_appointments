#!/usr/bin/env python

from setuptools import find_packages
from setuptools import setup  # type: ignore


setup(
    name='heb_vaccine',
    version='0.1.0',
    url='https://github.com/oldarmyc/vaccine_appointments',
    license='Apache License, Version 2.0',
    author='Dave Kludt',
    author_email='oldarmyc@gmail.com',
    description='Python library to assist with Covid19 HEB appointments',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=['requests'],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': ['heb-vaccine=heb_vaccine.schedule:main']
    },
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python'
    ]
)
