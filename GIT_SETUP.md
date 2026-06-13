# Git Ignore Guidelines

This project uses the following ignore files to keep the repository clean:

## .gitignore
- Python cache and compiled files (`__pycache__/`, `*.pyc`)
- Virtual environments (`venv/`, `env/`)
- IDE configurations (`.vscode/`, `.idea/`)
- Django database and media files (`db.sqlite3`, `/media/`)
- Environment variables (`.env` files)
- Debug and test scripts (optional)

## .gitattributes
- Ensures consistent line endings across platforms
- Specifies binary vs text files

## Files Tracked
- Source code (`.py` files)
- Configuration files (`manage.py`, `settings.py`)
- Documentation (`README.md`, `requirements.txt`)
- Asset files (HTML, CSS, JS in `/static/`)

## Before Committing

```bash
# Check what will be committed
git status

# View actual changes
git diff

# Add files to staging
git add .

# Commit with a message
git commit -m "Your commit message"
```

## Pushing to GitHub

```bash
# First time setup
git remote add origin <your-repo-url>
git branch -M main
git push -u origin main

# Subsequent pushes
git push origin main
```
