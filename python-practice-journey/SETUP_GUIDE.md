# Repository Setup Guide

This guide will help you set up your Python Practice Journey repository on GitHub.

## Step 1: Create Repository on GitHub

1. Go to [GitHub](https://github.com) and log in
2. Click the "+" icon in the top-right corner
3. Select "New repository"
4. Fill in the details:
   - **Repository name**: `python-practice-journey` (or your preferred name)
   - **Description**: "Daily Python practice from beginner to advanced"
   - **Visibility**: Public (recommended) or Private
   - **DO NOT** initialize with README (we already have one)
5. Click "Create repository"

## Step 2: Organize Your Files

Create this folder structure on your local machine:

```
python-practice-journey/
│
├── README.md
├── LICENSE
├── .gitignore
├── CONTRIBUTING.md
│
└── day-01/
    ├── README.md
    └── solution.py
```

## Step 3: Initialize Git Repository

Open your terminal and navigate to your project folder:

```bash
# Navigate to your project folder
cd path/to/python-practice-journey

# Initialize git repository
git init

# Add all files
git add .

# Create first commit
git commit -m "Initial commit: Day 1 - Clean & Filter Challenge"
```

## Step 4: Connect to GitHub

Replace `yourusername` and `python-practice-journey` with your actual GitHub username and repository name:

```bash
# Add remote repository
git remote add origin https://github.com/yourusername/python-practice-journey.git

# Push to GitHub
git branch -M main
git push -u origin main
```

## Step 5: Verify

1. Go to your repository on GitHub
2. You should see all your files uploaded
3. The README.md should be displayed on the main page

## Step 6: Update Personal Information

Don't forget to update these files with your information:

1. **README.md**: Replace `yourusername` with your GitHub username
2. **LICENSE**: Replace `[Your Name]` with your actual name
3. Add your LinkedIn or other social links if desired

## Daily Workflow

For each new day of practice:

```bash
# Create new day folder
mkdir day-02
cd day-02

# Create files
touch README.md solution.py

# After completing the challenge
git add .
git commit -m "Day 2: [Challenge Name]"
git push origin main
```

## Tips

- Commit frequently with descriptive messages
- Update the main README.md progress table after each day
- Tag your commits for milestones (e.g., `git tag -a week1 -m "Completed Week 1"`)
- Consider creating a GitHub Project board to track progress

## Troubleshooting

### Authentication Issues
If you encounter authentication issues, you may need to:
- Set up SSH keys ([GitHub Guide](https://docs.github.com/en/authentication/connecting-to-github-with-ssh))
- Or use a Personal Access Token ([GitHub Guide](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token))

### File Already Exists
If you initialized the repo with a README on GitHub:
```bash
git pull origin main --rebase
git push origin main
```

---

**Happy Coding! 🚀**
