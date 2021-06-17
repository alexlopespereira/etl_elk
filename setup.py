from distutils.core import setup

setup(
    name="etlelk",
    packages=['etlelk'],
    version="0.0.44",
    license="GNU Lesser General Public License v3.0",
    description="A small example package",
    author="Alex Lopes Pereira",
    author_email="alexlopespereira@gmail.com",
    url="https://github.com/alexlopespereira/etl_elk",
    download_url="https://github.com/alexlopespereira/etl_elk/archive/0.0.44.tar.gz",
    keywords=['elasticsearch', 'ETL'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    install_requires=[
        'bleach==3.2.0',
        'certifi>=2020.6.20',
        'cffi==1.14.3',
        'chardet==3.0.4',
        'cryptography==3.3.2',
        'docutils>=0.16',
        'elasticsearch==7.9.1',
        'elasticsearch-dsl==7.3.0',
        'idna>=2.10',
        'importlib-metadata==1.7.0',
        'jeepney==0.4.3',
        'keyring==21.4.0',
        'pkginfo==1.5.0.1',
        'pycparser==2.20',
        'Pygments==2.7.1',
        'readme-renderer==26.0',
        'requests>=2.24.0',
        'requests-toolbelt==0.9.1',
        'SecretStorage==3.1.2',
        'six>=1.15.0',
        'tqdm==4.49.0',
        'twine==3.2.0',
        'urllib3>=1.25.10',
        'webencodings==0.5.1',
        'zipp==3.1.0'
      ],
)
