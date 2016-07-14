import os
import re
from setuptools import setup


def read(path):
    with open(os.path.join(os.path.dirname(__file__), path), 'r') as f:
        data = f.read()
    return data.strip()


_version_re = re.compile(r'\s*__version__\s*=\s*\'(.*)\'\s*')
version = _version_re.findall(read('plank.py'))[0]


install_requires = read('requirements.txt').split('\n')
test_requires = read('build-requirements.txt').split('\n')
test_requires.extend(install_requires)

setup(
    name='plank',
    version=version,
    url='http://github.com/atbentley/plank/',
    license='MIT',
    author='Andrew Bentley',
    author_email='andrew.t.bentley@gmail.com',
    description="A simple task and build runner that doesn't get in the way.",
    long_description=read('README.rst'),
    py_modules=['plank'],
    entry_points={'console_scripts': ['plank = plank:plank_runner']},
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=install_requires,
    tests_require=test_requires,
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5'
    ]
)
