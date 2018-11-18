# Copyright (c) 2016-2018 John Mihalic <https://github.com/mezz64>
# Licensed under the MIT license.

# Used this guide to create module
# http://peterdowns.com/posts/first-time-with-pypi.html

# git tag 0.1 -m "0.1 release"
# git push --tags origin master
#
# Upload to PyPI Live
# python setup.py register -r pypi
# python setup.py sdist upload -r pypi


from distutils.core import setup
setup(
    name='pyHik',
    packages=['pyhik'],
    version='0.1.10',
    description='Provides a python api to interact with a Hikvision camera event stream.',
    author='John Mihalic',
    author_email='mezz64@users.noreply.github.com',
    url='https://github.com/shaibt/pyhik',
    download_url='https://github.com/shaibt/pyhik/tarball/0.1.10',
    keywords=['hik', 'hikvision', 'event stream', 'events', 'api wrapper', 'homeassistant'],
    classifiers=[],
    )
