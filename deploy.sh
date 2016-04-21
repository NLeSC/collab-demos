#!/bin/bash

# This file is based on the instructions I found here:
# https://gist.github.com/domenic/ec8b0fc8ab45f39403dd

# exit on any error
set -o errexit

# disallow unset variables
set -o nounset

# command to install dependencies
pip install -r requirements.txt

# Re-attach HEAD by checking out master
git checkout master

# call the python script that generates the readme.md
python3 src/makereadme.py

# commit the updated README.md
git add ./README.md
git commit --allow-empty -m "$(git config user.name): automatically generated README.md"

#git push git@github.com:${TRAVIS_REPO_SLUG}.git $TRAVIS_BRANCH
git push origin master:master
