#!/bin/bash
set -e # Exit with nonzero exit code if anything fails

# call the python script that generates the readme.md
python3 src/makereadme.py

