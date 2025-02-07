from setuptools import setup
from setuptools import find_packages

setup(
    name="deriver",
    description="Deriver: for all your molecule generation needs.",
    long_description="A software tool for the generation of novel chemical entities.",
    version="2.9.1",
    url="https://github.com/cyclica/deriver",
    license="All Rights Reserved Cyclica Inc.",
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "selfies==2.1.0",
        "peewee>=3.9.3",
        "numpy>=1.16.3",
        "crem==0.2.9",
        "loguru==0.6.0",
        "pandas>=1.0.*",
    ],
)
