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
├── day04/
│   ├── __init__.py
│   ├── async_intro.py
│   ├── create_task_intro.py
│   ├── final_async.py
│   └── review.py
├── day05/
│   ├── __init__.py
│   ├── .env.example
│   ├── architecture.py
│   ├── config.py
│   ├── main.py
│   └── handlers/
│       ├── __init__.py
│       └── commands.py
├── .env                  # Local secrets (not tracked by Git)
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

- Practiced exception handling with `try`, `except`, `else`, `finally`, and `raise`.
- Implemented order validation with input conversion and descriptive error messages.
- Tested valid and invalid input scenarios.
- Configured Python logging with `DEBUG`, `INFO`, and `WARNING` levels.
- Practiced logging application events and validation errors.
- Learned to manage environment variables using `python-dotenv`.
- Implemented configuration validation for `BOT_TOKEN` and `ADMIN_ID`.
- Protected sensitive configuration using `.gitignore` and `.env.example`.

### Day 4 — Asynchronous Programming with asyncio

- Learned the fundamentals of asynchronous programming and the Event Loop.
- Practiced defining coroutines using `async def` and `await`.
- Compared blocking `time.sleep()` with non-blocking `asyncio.sleep()`.
- Used `asyncio.gather()` to execute multiple coroutines concurrently.
- Created and managed individual tasks using `asyncio.create_task()`.
- Practiced coordinating concurrent operations and waiting for task completion.
- Simulated concurrent processing of multiple Telegram bot requests.

### Day 5 — Introduction to aiogram 3.x

- Learned the architecture of `Bot`, `Dispatcher`, and `Router`.
- Created a Telegram bot using BotFather.
- Connected the bot to the Telegram Bot API.
- Implemented secure token loading through environment variables.
- Used `bot.get_me()` to retrieve bot information.
- Started receiving updates through long polling.
- Implemented `/start` and `/help` command handlers.
- Practiced using `CommandStart` and `Command` filters.
- Added logging for application startup, shutdown, and incoming commands.
- Organized handlers into a separate Python package.
- Practiced registering routers with `Dispatcher.include_router()`.
- Used `if __name__ == "__main__"` to define the application entry point.

### Day 6 — Message Filters and Content Handling

- Learned to use `F` filters in aiogram 3.x.
- Implemented case-insensitive text message handlers.
- Handled incoming photos and documents.
- Retrieved document filenames from Telegram messages.
- Organized message handlers into separate routers.
- Learned how handler registration order affects message processing.
- Implemented a fallback handler for unknown messages.
- Practiced asynchronous message handling and logging.

## Technologies

- Python 3
- aiogram 3.x
- asyncio
- Python logging
- python-dotenv
- Git and GitHub
- Linux

## Setup and Installation

### 1. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the environment:

**Bash / Zsh:**

```bash
source .venv/bin/activate
```

**Fish shell:**

```fish
source .venv/bin/activate.fish
```

### 2. Install Dependencies

```bash
python -m pip install "aiogram>=3,<4" python-dotenv
```

### 3. Configure Environment Variables

Create a `.env` file in the project root.

Use `day05/.env.example` as a reference:

```dotenv
BOT_TOKEN=your_telegram_bot_token_here
```

Replace the placeholder with a token obtained from BotFather.

**Security:** Never commit real Telegram bot tokens, passwords, or other secrets to Git.

## Running the Exercises

Run commands from the project root.

### Day 1 — Python Fundamentals

```bash
python day01_diagnostics.py
```

### Day 2 — Modules and OOP

```bash
python -m day02.main
```

### Day 3 — Exception Handling and Logging

```bash
python -m day03.order_validation
python -m day03.order_logging
```

### Day 4 — Asyncio

```bash
python -m day04.async_intro
python -m day04.create_task_intro
python -m day04.final_async
python -m day04.review
```

### Day 5 — Telegram Bot

```bash
python -m day05.main
```

Once running, open the bot in Telegram and send:

- `/start` — Display the welcome message.
- `/help` — Display available commands.

The bot uses long polling to receive Telegram updates.

Press `Ctrl+C` to stop the bot.


## Project Status

**Day 6 of 30 — Completed**

The next stages of this training program will focus on advanced aiogram features, databases, API integrations, and deploying production-ready Telegram bots to Linux VPS servers.