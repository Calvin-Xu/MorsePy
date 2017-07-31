try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Morse code encoder & decoder',
    'author': 'Calvin Xu',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'calvinxu806@vip.163.com',
    'version': '1.0.0',
    'install_requires': ['pytest'],
    'packages': ['main'],
    'scripts': [],
    'name': 'morsepy'
}

setup(**config)
