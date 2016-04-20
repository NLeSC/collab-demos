#!/bin/bash

# This file is based on the instructions I found here:
# https://gist.github.com/domenic/ec8b0fc8ab45f39403dd

set -e # Exit with nonzero exit code if anything fails

# check that GH_USER has been set using Bash magic from
# http://stackoverflow.com/questions/3601515/how-to-check-if-a-variable-is-set-in-bash
if [ -z "${GH_USER:+x}" ]; then
    echo "GH_USER is unset. Aborting.";
    exit 1;
fi

# check that GH_TOKEN has been set using Bash magic from
# http://stackoverflow.com/questions/3601515/how-to-check-if-a-variable-is-set-in-bash
if [ -z "${GH_TOKEN:+x}" ]; then
    echo "GH_TOKEN is unset. Aborting.";
    exit 1;
fi

# check that GH_REPO has been set using Bash magic from
# http://stackoverflow.com/questions/3601515/how-to-check-if-a-variable-is-set-in-bash
if [ -z "${GH_REPO:+x}" ]; then
    echo "GH_REPO is unset. Aborting.";
    exit 1;
fi

# call the python script that generates the readme.md
python3 src/makereadme.py

# Commit the updated README.md
git add ./README.md
git commit -m "travis-ci: automatically generated README.md"

# Force push from the current repo's master branch to the remote
# repo's master branch. We redirect any output to /dev/null to hide any
# sensitive credential data that might otherwise be exposed.
git push --force --quiet "https://${GH_USER}:${GH_TOKEN}@${GH_REPO}" master:master > /dev/null 2>&1

