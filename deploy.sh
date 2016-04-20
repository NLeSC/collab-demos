#!/bin/bash

# This file is based on the instructions I found here:
# https://gist.github.com/domenic/ec8b0fc8ab45f39403dd

# exit on any error
set -o errexit

# disallow unset variables
set -o nounset

# call the python script that generates the readme.md
python3 src/makereadme.py

# Commit the updated README.md
git add ./README.md
git commit -m "travis-ci: automatically generated README.md"

# push from the current repo's master branch to the remote
# repo's master branch.


# works, ask for username and password:
# git push origin master

git push https://github.com/jspaaks/collab-demos.git master


# should work
# git push "https://${GH_USER}:${GH_TOKEN}@${GH_REF}" master:master
