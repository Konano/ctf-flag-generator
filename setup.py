import setuptools
from pathlib import Path

import flag_gen

LONG_DESC = Path('README.md').read_text('utf8')
VERSION = flag_gen.__version__

setuptools.setup(
    name='flag_gen',
    packages=setuptools.find_packages(),
    version=VERSION,
    license='MIT',
    description='A CTF leet flag generator',
    long_description=LONG_DESC,
    long_description_content_type="text/markdown",
    author='Konano',
    author_email='w@nano.ac',
    url='https://github.com/Konano/ctf-flag-generator',
    keywords=['ctf', 'flag', 'generator'],
    install_requires=[],
    entry_points={'console_scripts': ['flag-gen=flag_gen.__main__:main']},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Security',
        'Topic :: Security :: Cryptography',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
)
