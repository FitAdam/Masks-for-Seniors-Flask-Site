import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="localmask-pkg-FitAdam", 
    version="0.0.1",
    author="FitAdam",
    author_email="a.tutakiewicz@gmail.com",
    description="A package to run flask site for covid19 masks",
    url="https://github.com/FitAdam/Masks-for-Seniors-Flask-Site",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)