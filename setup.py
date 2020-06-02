# setup.py file

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="lambdata-davidcruz0202", # the name that you will install via pip
    version="1.1",
    author="David Cruz",
    author_email="dcman1211@gmail.com",
    description="my first package",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/DAVIDCRUZ0202/lambdata-davidcruz0202",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)