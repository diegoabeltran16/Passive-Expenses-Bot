#!/bin/bash

# Exit on any error
set -e
set -x  # Enable debugging output

# Check if a hotfix branch name is provided
if [ -z "$1" ]; then
  echo "Error: No hotfix branch name provided."
  echo "Usage: ./sync_hotfix.sh <hotfix-branch-name>"
  exit 1
fi

HOTFIX_BRANCH=$1

# Call sync_branch.sh with the hotfix branch
./sync_branch.sh $HOTFIX_BRANCH
