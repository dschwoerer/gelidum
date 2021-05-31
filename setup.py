import os
from setuptools import setup

root_dir_path = os.path.dirname(os.path.abspath(__file__))

long_description = open(os.path.join(root_dir_path, "LONGDESC.rst")).read()

requirements_path = os.path.join(root_dir_path, "requirements.txt")
with open(requirements_path) as requirements_file:
    requirements = requirements_file.readlines()

setup(
    name="gelidum",
    version="0.1",
    author="Diego J. Romero López",
    author_email="diegojromerolopez@gmail.com",
    description="Freeze your python objects",
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License"
    ],
    install_requires=requirements,
    license="MIT",
    keywords="freeze python object",
    url="https://github.com/diegojromerolopez/gelidum",
    packages=["gelidum"],
    package_dir={"gelidum": "gelidum"},
    data_files=[],
    include_package_data=True,
    scripts=[]
)
