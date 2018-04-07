"""
Mapreduce python modules.

Amy Chern <chernamy@umich.edu>
Nilay Muchhala <nilaym@umich.edu>
"""

from setuptools import setup

setup(
    name='mapreduce',
    version='0.1.0',
    packages=['mapreduce'],
    include_package_data=True,
    install_requires=[
        'click==6.7',
        'sh==1.12.14',
        'pylint==1.7.2',
        'pydocstyle==2.0.0',
        'pycodestyle==2.3.1',
    ],
    entry_points={
        'console_scripts': [
            'mapreduce-master = mapreduce.master.__main__:main',
            'mapreduce-worker = mapreduce.worker.__main__:main',
            'mapreduce-submit = mapreduce.submit:main',
        ]
    },
)
