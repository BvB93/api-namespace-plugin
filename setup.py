import os
from setuptools import setup

version = {}
version_path = os.path.join('array_namespace', '__version__.py')
with open(version_path, 'r', encoding='utf-8') as f:
    exec(f.read(), version)

with open('README.rst', 'r', encoding='utf-8') as f:
    readme = f.read()

setup(
    name='array_namespace',
    version=version['__version__'],
    description=('Experimental mypy plugin for the Array-API '
                 '`__array_namespace__` protocol.'),
    long_description=f'{readme}\n\n',
    long_description_content_type='text/x-rst',
    author=['Bas van Beek'],
    author_email='bas.vanbeek@hotmail.com',
    url='https://github.com/BvB93/api-namespace-plugin',
    packages=['array_namespace'],
    package_data={'array_namespace': ['py.typed']},
    include_package_data=True,
    license='Apache License',
    zip_safe=False,
    keywords=[
        "annotations",
        "checker",
        "checking",
        "hinting",
        "hints",
        "type",
        "typechecking",
        "typehinting",
        "typehints",
        "typing",
        "mypy",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development",
        "Typing :: Typed",
    ],
    python_requires='>=3.6',
    install_requires=['mypy'],
    extras_require={'tests': ['pytest']}
)
