from setuptools import setup

setup(
    name='snapshotalyzer-50000',
    version='0.1',
    author="Falcon",
    description='snapshotalyzer 50000 is a tool to manage AWS EC2 snapshots',
    packages=['shotty'],
    url="https://github.com/CChapmanCBS/snapshotalyzer-50000",
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
    ''',
)
