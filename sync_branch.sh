#!/bin/bash

# Exit on any error
set -e
set -x  # Enable debugging output

# Set environment variables
export GITHUB_TOKEN=your_github_token
export GITHUB_REPO=github.com/diegoabeltran16/Passive-Expenses-Bot.git
export GITLAB_TOKEN=your_github_token
export GITLAB_REPO=gitlab.com/business-cash-flow/Passive-Expenses-Bot.git
export BRANCH_NAME=your_branch_name  # Replace with the branch name you want to sync

# Configure Git credential helper to store credentials temporarily
git config --global credential.helper cache

# Print environment variables for debugging
echo "GITHUB_REPO: ${GITHUB_REPO}"
echo "GITLAB_REPO: ${GITLAB_REPO}"
echo "BRANCH_NAME: ${BRANCH_NAME}"

# Verify that environment variables are set
if [ -z "$BRANCH_NAME" ]; then
  echo "Error: BRANCH_NAME is not set"
  exit 1
fi

# Configure Git
git config --global user.email "diegobeltran1016@gmail.com"
git config --global user.name "Diego Alejandro Beltran"

# Remove remotes if they exist (to ensure clean state)
git remote remove github || true
git remote remove gitlab || true

# Add GitHub as a remote
git remote add github "https://${GITHUB_TOKEN}@${GITHUB_REPO}"
echo "GitHub remote added."

# Add GitLab as a remote
git remote add gitlab "https://${GITLAB_TOKEN}@${GITLAB_REPO}"
echo "GitLab remote added."

# Fetch all branches from both remotes
echo "Fetching branches from GitHub..."
git fetch github || echo "Failed to fetch from GitHub. Check the repository URL and token permissions."
echo "Fetching branches from GitLab..."
git fetch gitlab || echo "Failed to fetch from GitLab. Check the repository URL and token permissions."

# Checkout the specific branch
git checkout ${BRANCH_NAME}

# Ensure changes are committed locally
echo "Checking for local changes..."
git status
if ! git diff-index --quiet HEAD --; then
  echo "Staging all changes..."
  git add -A  # Add all changes (tracked, untracked, and deletions)
  echo "Committing local changes..."
  git commit -m "Automated commit by sync script"
fi

# Merge changes from GitHub to GitLab
echo "Merging changes from GitHub to GitLab..."
if git pull github ${BRANCH_NAME}; then
  echo "Pulled changes from GitHub successfully."
else
  echo "Failed to pull changes from GitHub."
fi
if git push gitlab ${BRANCH_NAME}; then
  echo "Pushed changes to GitLab successfully."
else
  echo "Failed to push changes to GitLab."
fi

# Merge changes from GitLab to GitHub
echo "Merging changes from GitLab to GitHub..."
if git pull gitlab ${BRANCH_NAME}; then
  echo "Pulled changes from GitLab successfully."
else
  echo "Failed to pull changes from GitLab."
fi
if git push github ${BRANCH_NAME}; then
  echo "Pushed changes to GitHub successfully."
else
  echo "Failed to push changes to GitHub."
fi

echo "Sync process for ${BRANCH_NAME} completed."
