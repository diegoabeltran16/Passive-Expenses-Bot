#!/bin/bash

# Exit on any error
set -e
set -x  # Enable debugging output

# Set environment variables
export GITHUB_TOKEN=your_github_token
export GITHUB_REPO=github.com/diegoabeltran16/Passive-Expenses-Bot.git
export GITLAB_TOKEN=your_github_token
export GITLAB_REPO=gitlab.com/business-cash-flow/Passive-Expenses-Bot.git

# Configure Git credential helper to store credentials temporarily
git config --global credential.helper cache

# Configure Git
git config --global user.email "diegobeltran1016@gmail.com"
git config --global user.name "Diego Alejandro Beltran"

# Remove remotes if they exist (to ensure clean state)
git remote remove github || true
git remote remove gitlab || true

# Add GitHub and GitLab remotes
git remote add github "https://${GITHUB_TOKEN}@${GITHUB_REPO}"
git remote add gitlab "https://${GITLAB_TOKEN}@${GITLAB_REPO}"

# Fetch all branches
git fetch github
git fetch gitlab

# Checkout cycle-1 branch
git checkout cycle-1

# Merge all feature branches into cycle-1
for branch in $(git branch --list "feature/*"); do
  git merge $branch --no-ff -m "Merge feature $branch into cycle-1"
done

# Push changes to GitHub and GitLab
git push github cycle-1 || echo "Failed to push to GitHub."
git push gitlab cycle-1 || echo "Failed to push to GitLab."

echo "All feature branches merged into cycle-1 and synchronized."
