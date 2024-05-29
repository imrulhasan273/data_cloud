#!/bin/bash

# Add all changes to staging
git add .

# Commit changes with a timestamp
git commit -m "Changes committed at $(date)"

# Push to the master branch
git push origin master