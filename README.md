# Telegram Bot Development Training

This repository contains my practical exercises and projects from a **30-day intensive Python Telegram bot development program**.

The main goal is to develop practical skills in building reliable, asynchronous Telegram bots using Python and aiogram 3.x, with a focus on real-world projects and freelance development.

## Learning Goals

- Improve Python programming skills.
- Learn asynchronous programming with asyncio.
- Develop Telegram bots using aiogram 3.x.
- Work with SQLite and PostgreSQL.
- Integrate external REST APIs.
- Implement error handling, logging, and configuration management.
- Practice Git and GitHub.
- Deploy Telegram bots to Linux VPS servers.
- Build a portfolio of practical projects.

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
├── day06/
│   ├── __init__.py
│   ├── main.py
│   └── handlers/
│       ├── __init__.py
│       ├── text.py
│       ├── media.py
│       └── fallback.py
├── day07/
│   ├── __init__.py
│   ├── main.py
│   ├── first_request.py
│   ├── error_handling.py
│   ├── handlers/
│   │   ├── __init__.py
│   │   └── todo.py
│   └── services/
│       ├── __init__.py
│       └── todo_api.py
├── .env                  # Local secrets (not tracked by Git)
├── .gitignore
└── README.md
```

## Learning Progress

### Day 1 — Python Fundamentals

- Practiced functions, loops, lists, and dictionaries.
- Implemented user search and statistics.
- Created the `SupportTicket` class.
- Practiced object-oriented programming.
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

### Day 7 — HTTP, JSON and REST API Integration

- Learned HTTP fundamentals and common request methods: `GET`, `POST`, `PUT`, `PATCH`, and `DELETE`.
- Studied HTTP status codes, including `200`, `404`, and `500`.
- Practiced JSON deserialization and serialization using `json.loads()` and `json.dumps()`.
- Learned to make asynchronous HTTP requests using `aiohttp`.
- Used `aiohttp.ClientSession` and asynchronous context managers.
- Parsed JSON responses using `await response.json()`.
- Validated HTTP responses using `response.raise_for_status()`.
- Configured request timeouts using `aiohttp.ClientTimeout`.
- Practiced handling HTTP errors, connection errors, and timeouts.
- Integrated an external REST API into an aiogram Telegram bot.
- Separated API communication into a service module.
- Implemented the `/todo` command to retrieve task data from JSONPlaceholder.
- Added logging and user-friendly error messages.
- Tested successful API responses and HTTP 404 error handling.

#### Day 7 Project — Telegram Todo Bot

A Telegram bot that retrieves task information from the JSONPlaceholder REST API and displays it to the user.

**Features:**

- `/todo` — Fetch and display a task from an external REST API.
- Asynchronous HTTP requests using `aiohttp`.
- JSON response parsing.
- HTTP status validation.
- Request timeout configuration.
- Handling of HTTP errors, connection errors, and timeouts.
- Logging of commands and API exceptions.
- Separation of Telegram handlers and API services.

**Architecture:**

```text
Telegram User
      |
      v
aiogram Dispatcher
      |
      v
Todo Handler
(day07/handlers/todo.py)
      |
      v
API Service
(day07/services/todo_api.py)
      |
      v
JSONPlaceholder REST API
      |
      v
JSON Response
      |
      v
Telegram Message
```

**Example successful response:**

```text
📋 Task: molestiae perspiciatis ipsa
✅ Done: False
```

**Example HTTP error response:**

```text
Response error 404
```

The project demonstrates how a Telegram bot can communicate with an external service while keeping API communication separate from message-handling logic.

## Technologies

- Python 3
- aiogram 3.x
- aiohttp
- asyncio
- Python logging
- python-dotenv
- REST APIs
- JSON
- Git and GitHub
- Linux

## Setup and Installation

### 1. Clone the Repository

```bash
git clone https://github.com/javohir-kadirov/telegram-bot-training.git
cd telegram-bot-training
```

### 2. Create a Virtual Environment

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

### 3. Install Dependencies

```bash
python -m pip install "aiogram>=3,<4" aiohttp python-dotenv
```

### 4. Configure Environment Variables

Create a `.env` file in the project root.

Use `day05/.env.example` as a reference:

```dotenv
BOT_TOKEN=your_telegram_bot_token_here
```

Replace the placeholder with a token obtained from BotFather.

**Security:** Never commit real Telegram bot tokens, passwords, or other secrets to Git.

The `.env` file must remain excluded from version control.

## Running the Exercises

Run all commands from the project root with the virtual environment activated.

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

### Day 6 — Message Filters

```bash
python -m day06.main
```

Test the bot by sending text messages, photos, documents, and unsupported messages.

### Day 7 — REST API Integration

Run the standalone HTTP examples:

```bash
python -m day07.first_request
python -m day07.error_handling
```

Start the Telegram Todo Bot:

```bash
python -m day07.main
```

Open the bot in Telegram and send:

- `/todo` — Retrieve and display a task from JSONPlaceholder.

If the external API returns an error, the bot responds with an error message instead of silently failing.

The bot uses long polling to receive Telegram updates.

Press `Ctrl+C` to stop a running bot.

**Note:** Run only one polling process for the same Telegram bot token at a time.

## Project Status

**Day 7 of 30 — Practical Tasks Completed**

Completed topics:

- Python fundamentals and OOP
- Modules, type hints, and Git
- Exception handling and logging
- Asynchronous programming with asyncio
- Telegram bot development using aiogram 3.x
- Message filtering and content handling
- HTTP, JSON, and external REST API integration

**Next steps:**

Continue developing more advanced Telegram bot functionality, including structured user interactions, databases, and progressively more realistic projects.

The long-term goal is to build production-ready Telegram bots and develop a portfolio suitable for freelance work.