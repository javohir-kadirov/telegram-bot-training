# Telegram Bot Development Training

This repository contains my practical exercises and projects from a 30-day intensive Python Telegram bot development program.

## Learning Goals

- Improve Python programming skills.
- Learn asynchronous programming with asyncio.
- Develop Telegram bots using aiogram 3.x.
- Work with SQLite and PostgreSQL.
- Integrate external APIs.
- Practice Git and GitHub.
- Deploy Telegram bots to Linux VPS servers.

## Project Structure

```text
telegram-bot-training/
├── day01_diagnostics.py
├── day02/
│   ├── __init__.py
│   ├── main.py
│   ├── users.py
│   └── tickets.py
├── day03/
│   ├── __init__.py
│   ├── .env.example
│   ├── config.py
│   ├── order_validation.py
│   └── order_logging.py
├── .env                  # Local configuration (not tracked by Git)
├── .gitignore
└── README.md
```

## Learning Progress

### Day 1 — Python Fundamentals

- Practiced functions, loops, lists, and dictionaries.
- Implemented user search and statistics.
- Created the `SupportTicket` class.
- Configured a Python virtual environment and Git.

### Day 2 — Python Modules and GitHub

- Organized Python code into modules and packages.
- Practiced absolute imports.
- Added type hints to functions and classes.
- Learned Git commits, branches, and remote repositories.
- Practiced resolving merge conflicts.
- Published the project on GitHub.

### Day 3 — Exception Handling, Logging and Configuration

- Learned exception handling with `try`, `except`, `else`, `finally`, and `raise`.
- Implemented order validation with input conversion and custom error messages.
- Tested valid and invalid input scenarios.
- Configured Python logging with `DEBUG`, `INFO`, and `WARNING` levels.
- Practiced logging application events and validation errors.
- Learned to manage environment variables using `python-dotenv`.
- Implemented configuration validation for `BOT_TOKEN` and `ADMIN_ID`.
- Protected sensitive configuration using `.gitignore` and `.env.example`.

## Technologies

- Python 3
- Git and GitHub
- Linux
- Python logging
- python-dotenv

## Running the Exercises

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

For Fish shell:

```fish
source .venv/bin/activate.fish
```

Install the configuration dependency:

```bash
python -m pip install python-dotenv
```

Run the exercises from the project root:

```bash
python day01_diagnostics.py
python -m day02.main
python -m day03.order_validation
python -m day03.order_logging
```

## Environment Configuration

Create a `.env` file in the project root using `day03/.env.example` as a reference.

Use test values for the current exercises. Never commit real Telegram bot tokens, passwords, or other secrets.

## Status

**Day 3 of 30 — Final Git verification pending.**

This repository will continue to grow as I learn aiogram 3.x, databases, API integrations, and VPS deployment.