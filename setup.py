from setuptools import find_packages,setup

from typing import List


def get_requirements():
    with open("requirements.txt") as file:
        return [
            req.strip()
            for req in file
            if req.strip() and req.strip() != "-e ."
        ]

setup(
    name='APS',
    version="0.0.1",
    author="Manthan",
    author_email="bhisemanthan985@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)