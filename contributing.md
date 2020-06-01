# Contributor's Guide

# Installation

Git clone and navigate to the repo from your command-line:

``` sh
git clone REMOTE_ADDRESS
cd /path/to/repo
```

Create / Activate a virtual environment:

```sh
pipenv --python 3.7 # creates a new virtual env for the first time, also creates Pipfile
pipenv install pandas # installs a given package inside the virtual env, creates a Pipfile.lock if installing something for the first time, and auto-adds pandas to the Pipfile and Pipfile.lock
pipenv shell # activates the virtual env
```