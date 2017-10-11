#!/bin/bash

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

# add, commit, and push the updated README.md
git add ./README.md
git commit --allow-empty -m "$(git config user.name): automatically generated README.md"

# not sure this will work but removing this file might resolve issue
# https://github.com/NLeSC/collab-demos/issues/104
# see https://github.com/git-lfs/git-lfs/issues/2291
rm .git/hooks/pre-push

git push origin master:master
