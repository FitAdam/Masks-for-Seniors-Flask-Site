from setuptools import setup

setup(
    name='LocalMask',
    packages=['mask-site'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)