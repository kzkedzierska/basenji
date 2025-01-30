from pathlib import Path
from setuptools import setup, find_packages

with open("README.md", encoding="utf-8") as f:
    readme = f.read()

with open("LICENSE", encoding="utf-8") as f:
    license = f.read()

setup(
    name="basenji",
    version="0.1",
    description="Sequential regulatory activity machine learning",
    long_description=readme,
    author="David Kelley",
    author_email="drk@calicolabs.com",
    url="https://github.com/calico/basenji",
    license=license,
    packages=find_packages(exclude=("tests", "docs")),
    include_package_data=True,
    install_requires=[
        line.strip()
        for line in Path("requirements.txt")
        .read_text(encoding="utf-8")
        .splitlines()
        if line.strip() and not line.startswith("#")
    ],
    zip_safe=False,
)
