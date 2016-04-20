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

# git lfs struggles with urls, apparently, so need to use named remotes

if git remote | grep togithub > /dev/null; then

    echo "remote 'togithub' exists. No need to add it."

else

    # note: this adds plaintext credentials to the Travis'es .git config file
    git remote add togithub https://${GH_USER}:${GH_TOKEN}@${GH_REPO}

fi

# use the named remote to push to. Also, make the command as quiet as possible
# using '--quiet' and '> /dev/null 2>&1' to avoid accidentally outputting
# credentials, which may end up in a log somewhere.
git push --quiet togithub master:master > /dev/null 2>&1

# delete the 'togithub' remote for *marginally* better security
git remote rm togithub
