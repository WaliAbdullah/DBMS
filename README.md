# 🐍 DBMS Flask + MySQL Demo

A simple Python project to demonstrate:
- Connecting to a MySQL database using `mysql-connector-python`
- Listing and displaying table contents
- Running a web UI with Flask
- Managing dependencies using **Poetry**

---

## 📁 Project Structure

```
dbms/
├── app/
│   ├── __init__.py         # Package marker
│   ├── main.py             # CLI script to print table names
│   ├── webapp.py           # Flask app to show all tables + data
│   └── templates/
│       └── index.html      # HTML template used by Flask
├── env.sh                  # Script to setup virtual environment
├── pyproject.toml          # Poetry dependency manager config
├── poetry.lock             # Exact package versions
└── README.md               # This file
```

---

## ✅ Prerequisites

- Python **3.10+**
- MySQL server running at:
  - Host: `127.0.0.1`
  - Port: `33061`
  - User: `root`
  - Password: `123456`
  - Database: `test_db`

---

## 🔧 Step 1: Install Poetry (If Not Installed)

> Poetry is a modern Python dependency and environment manager.

Install it using:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Then add Poetry to your shell profile (if not auto-done):

```bash
export PATH="$HOME/.local/bin:$PATH"
```

Check it works:

```bash
poetry --version
```

---

## 📦 Step 2: Setup the Environment

Run the provided setup script:

```bash
source env.sh
```

This will:
- Create a virtual environment at `.venv/`
- Activate it
- Install dependencies using Poetry

> If the script fails, you can run the steps manually:

```bash
# Create virtual environment
python3.10 -m venv .venv

# Activate it
source .venv/bin/activate

# Install Poetry inside the venv
pip install poetry

# Install project dependencies
poetry install
```

---

## 🧪 Step 3: Run the CLI Script

To list tables in the MySQL database:

```bash
poetry run python app/main.py
```

Expected output:

```
Tables in database:
- students
- instructors
...
```

---

## 🌐 Step 4: Run the Flask Web App

To start the web server:

```bash
poetry run python app/webapp.py
```

Then open your browser to:

```
http://localhost:5000
```

You will see:
- A list of all tables in the database
- The contents (rows and columns) of each table displayed inline

---

## 🛠 Troubleshooting

### ⚠️ TemplateNotFound

Make sure `templates/index.html` exists and is in the correct place (`templates/` at project root or inside `app/` depending on your config).

### ⚠️ MySQL Connection Error

Make sure your database matches the expected config:

```bash
mysql -u root -p123456 -h 127.0.0.1 -P 33061
```

Database name must be `test_db`.

### ⚠️ Port Already in Use

If Flask won’t start on port `5000`:

```bash
lsof -i :5000
kill <PID>
```

---

## 📌 Notes

- Project uses [Poetry](https://python-poetry.org/)
- Python: `^3.10`
- Flask: `^3.0.0`
- MySQL Connector: `^8.0`

---

## 📃 License

MIT — use freely for learning or teaching purposes.
