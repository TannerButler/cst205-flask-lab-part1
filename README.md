# CST 205 — Flask, Part 1

## Set up

```bash
python -m venv .venv
```

Windows PowerShell:
```powershell
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -c "import flask"
python app.py
```

macOS / Linux:
```bash
source .venv/bin/activate
pip install -r requirements.txt
python -c "import flask"
python app.py
```

Visit:
- `http://127.0.0.1:5000/` — Task 2 (no template)
- `http://127.0.0.1:5000/tanner` — Task 3 (Jinja template)
- `http://127.0.0.1:5000/photo` — Task 4 (Bootstrap + remote Picsum image)

Before submission, replace the **three sample classmates and acronyms** in `app.py` with answers from three actual classmates. Capture screenshots of all three pages **running locally in your own browser**. The supplied `previews/` folder is illustrative only and does not constitute proof that you ran the Flask app.

## Publish to GitHub
Create a new repository, then run:

```bash
git init
git add app.py templates requirements.txt .gitignore README.md
git commit -m "Complete CST 205 Flask Part 1 lab"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
git push -u origin main
```

Include the GitHub repository URL and three genuine browser screenshots with your Canvas submission.
