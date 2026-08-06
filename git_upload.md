# GitHub Upload Guide

This guide explains how to upload your project to GitHub using Git.

---

# 1. Open the project folder

```bash
cd "E:\GenAi-Project-Udemy\Code_15042025\Code_15042025"
```

---

# 2. Verify Git is installed

```bash
git --version
```

---

# 3. Initialize Git (only if this is a new project)

```bash
git status
git init
```

---

# 4. Create the `.gitignore` file (**Do this immediately after `git init` and before `git add .`**)

Create the file in PowerShell:

```powershell
New-Item -ItemType File -Path .gitignore -Force | Out-Null
notepad .gitignore
```

Paste the following:

```gitignore
# Python
__pycache__/
*.py[cod]

# Virtual Environment
.venv/
venv/
env/

# Environment Variables
.env
.env.*

# Jupyter
.ipynb_checkpoints/

# Testing
.pytest_cache/
.coverage
htmlcov/

# Logs
*.log

# IDEs
.vscode/
.idea/

# OS Files
.DS_Store
Thumbs.db

# Build Files
build/
dist/
*.egg-info/
.cache/
```

Save and close the file.

> **Why create `.gitignore` first?**
>
> Creating `.gitignore` before `git add .` prevents temporary files, virtual environments, secrets, cache files, and IDE settings from being tracked or uploaded to GitHub.

---

# 5. Verify Git status

```bash
git status
```

---

# 6. Connect the GitHub repository

```bash
git remote add origin https://github.com/aamir490/use-case-2---Building-a-Chatbot-using-Amazon-Bedrock-Langchain-Streamlit.git
```

If the remote already exists:

```bash
git remote set-url origin https://github.com/aamir490/use-case-2---Building-a-Chatbot-using-Amazon-Bedrock-Langchain-Streamlit.git
```

Verify:

```bash
git remote -v
```

---

# 7. Rename the branch to `main`

```bash
git branch -M main
```

---

# 8. Stage all project files

```bash
git add .
git status 
```

---

# 9. Verify staged files

```bash
git status
```

---

# 10. Create the first commit

```bash
git commit -m "Initial commit"
```

---

# 11. Push the project to GitHub

```bash
git push -u origin main
```

---

# 12. Verify the upload

Check the repository in your browser and confirm that:

* All required files are uploaded.
* The `main` branch exists.
* The latest commit is visible.

---

# If you created `.gitignore` after running `git add .`

If Git has already started tracking files that should be ignored, remove them from the Git index and stage the files again:

```bash
git rm -r --cached .
git add .
git commit -m "Apply .gitignore"
git push
```

---

# Recommended Workflow

```text
Open Project Folder
        │
        ▼
git init
        │
        ▼
Create .gitignore
        │
        ▼
git status
        │
        ▼
git remote add origin <GitHub Repository URL>
        │
        ▼
git branch -M main
        │
        ▼
git add .
        │
        ▼
git status
        │
        ▼
git commit -m "Initial commit"
        │
        ▼
git push -u origin main
```

---

# Best Practices

* Create `.gitignore` immediately after `git init`.
* Never upload `.env` files containing secrets.
* Never upload `.venv` or other virtual environments.
* Always check `git status` before committing.
* Use clear, descriptive commit messages.
* Verify the repository on GitHub after every push.
