from setuptools import setup, find_packages

version_parts = (0, 1, 0)
version = '.'.join(map(str, version_parts))

setup(
    name='$name$',
    description='$desc$',
    version=version,
    author='$author$',
    author_email='$email$',
    license='MIT',
    url='$url$',
    packages=find_packages(
        exclude=['unit', 'unit.*', 'integration', 'integration.*']),
    install_requires=[
        'ribosome',
    ]
)
