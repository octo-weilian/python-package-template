from setuptools import setup,find_packages
from pathlib import Path

requires = Path("requirements.txt")
if requires.exists():
    with open(requires) as f:
        dependencies = f.read().splitlines()

    setup(
        name = 'my-app',
        version = '0.1.0',
        description = 'A Python package',
        url = 'https://github.com/octo-willy/my-app',
        author = 'octo-willy',
        author_email='author@email.com',
        license = 'BSD 2-clause',
        packages = find_packages(),
        install_requires = dependencies,
        classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers'
        ]

    )

