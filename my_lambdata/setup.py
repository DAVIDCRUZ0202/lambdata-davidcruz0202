# setup.py file

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="Project_1", # the name that you will install via pip
    version="1.0",
    author="David_Cruz",
    author_email="dcman1211@gmail.com",
    description="first_project",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/YOUR_USERNAME/YOUR_REPO_NAME",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)