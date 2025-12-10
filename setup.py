"""Installation script for the 'leglab_scripts' python package."""

from setuptools import setup

setup(
    name="leglab_scripts",
    version="0.1.0",
    packages=["leglab_scripts"],
    package_dir={"leglab_scripts": "scripts"},
    author="Minh",
    maintainer="Minh",
    description="Training and evaluation scripts for the LegLab Isaac Lab extension.",
    url="https://github.com/supaz022002/LegLab",
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
    include_package_data=True,
    zip_safe=False,
)
