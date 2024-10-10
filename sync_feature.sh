#!/bin/bash

# Exit on any error
set -e
set -x  # Enable debugging output

# Check if a branch name is provided
if [ -z "$1" ]; then
  echo "Error: No branch name provided."
  echo "Usage: ./sync_branch.sh <branch-name>"
  exit 1
fi

BRANCH=$1

# Set environment variables
export GITHUB_TOKEN=your_github_token
export GITHUB_REPO=github.com/diegoabeltran16/Passive-Expenses-Bot.git
export GITLAB_TOKEN=your_gitlab_token
export GITLAB_REPO=gitlab.com/business-cash-flow/Passive-Expenses-Bot.git

# Configure Git credential helper to store credentials temporarily
git config --global credential.helper cache

# Configure Git
git config --global user.email "diegobeltran1016@gmail.com"
git config --global user.name "Diego Alejandro Beltran"

# Remove remotes if they exist (to ensure a clean state)
git remote remove github || true
git remote remove gitlab || true

# Add GitHub and GitLab remotes
git remote add github "https://${GITHUB_TOKEN}@${GITHUB_REPO}"
git remote add gitlab "https://${GITLAB_TOKEN}@${GITLAB_REPO}"

# Fetch branches
git fetch github
git fetch gitlab

# Checkout the branch
git checkout $BRANCH

# Sync from GitHub to GitLab
git pull github $BRANCH || echo "Failed to pull from GitHub."
git push gitlab $BRANCH || echo "Failed to push to GitLab."

# Sync from GitLab to GitHub
git pull gitlab $BRANCH || echo "Failed to pull from GitLab."
git push github $BRANCH || echo "Failed to push to GitHub."

echo "Branch '$BRANCH' synchronization completed."
