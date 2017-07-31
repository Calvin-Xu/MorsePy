try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Morse code encoder & decoder',
    'author': 'Calvin Xu',
    'url': 'https://github.com/Calvin-Xu/MorsePy',
    'download_url': 'https://github.com/Calvin-Xu/MorsePy',
    'author_email': 'calvinxu806@vip.163.com',
    'version': '1.1.0',
    'install_requires': ['pytest'],
    'packages': ['morsepy'],
    'scripts': [],
    'name': 'morsepy'
}

setup(**config)
