#!/bin/bash

# Exit on any error
set -e
set -x  # Enable debugging output

# Check if a feature branch name is provided
if [ -z "$1" ]; then
  echo "Error: No feature branch name provided."
  echo "Usage: ./sync_feature.sh <feature-branch-name>"
  exit 1
fi

FEATURE_BRANCH=$1

# Call sync_branch.sh with the feature branch
./sync_branch.sh $FEATURE_BRANCH
