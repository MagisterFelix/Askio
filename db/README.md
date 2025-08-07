# 🗃️ DB

The `DB` provides the asynchronous data layer for the system. It integrates with a PostgreSQL database and communicates with other components using RabbitMQ via FastStream. All interactions with the database are handled asynchronously using SQLAlchemy with asyncio support.

---

## 🧠 Responsibilities

* Define and manage the project's database models and schemas
* Perform asynchronous CRUD operations on PostgreSQL
* Consume events from RabbitMQ and apply corresponding DB actions
* Emit DB-related events to other components when necessary

---

## ⚙️ Technologies

| Layer         | Tool                          |
| ------------- | ----------------------------- |
| Database      | PostgreSQL \[asyncpg]         |
| ORM           | SQLAlchemy \[asyncio]         |
| Messaging     | FastStream \[RabbitMQ]        |
| Configuration | Pydantic \[pydantic-settings] |
| Async Runtime | Python asyncio                |

---

## 🏗️ Architecture

* **Async-First Design**: All DB access and event handling is fully asynchronous.
* **Event-Driven**: Subscribes to and reacts to events over RabbitMQ using FastStream.
* **Decoupled**: Interacts with other services purely through messages (no direct API coupling).
* **Modular Layout**: Models, brokers, and event handlers are logically separated.

---

## 📁 Internal Structure

```text
db
├── src
│   ├── models
│   │   ├── __init__.py       # model package init
│   │   ├── query.py          # query model definition
│   │   └── session.py        # session model definition
│   ├── __init__.py           # app package init
│   ├── base.py               # declarative base class for models
│   ├── crud.py               # CRUD functions
│   └── database.py           # engine and session setup
├── .python-version           # python version lock
├── broker.py                 # message broker setup
├── config.py                 # configuration loading
├── Dockerfile                # container image definition
├── main.py                   # entry point
├── pyproject.toml            # build system and dependencies
├── README.md                 # documentation
└── uv.lock                   # `uv` dependency lock file
```

---

## 📝 Notes

* Uses `SQLAlchemy` with `asyncpg` driver for PostgreSQL
* Message subscriptions are declared via decorators using FastStream
* Designed to be lightweight, reactive, and robust under async workflows
