# 💬 Chat

The `Chat` handles AI-powered chat responses using an event-driven, fully asynchronous architecture. It integrates with **Ollama** for local LLM inference and communicates with other components via **RabbitMQ** using **FastStream**.

---

## 🧠 Responsibilities

* Consume chat request events via RabbitMQ
* Generate responses using a local Ollama model
* Emit chat responses back to the system
* Operate in a fully asynchronous, event-driven manner

---

## ⚙️ Technologies

| Layer         | Tool                          |
| ------------- | ----------------------------- |
| LLM Engine    | Ollama                        |
| Messaging     | FastStream \[RabbitMQ]        |
| Configuration | Pydantic \[pydantic-settings] |
| Async Runtime | Python asyncio                |

---

## 🏗️ Architecture

* **Event-Driven**: Listens to chat-related messages and produces responses via RabbitMQ.
* **LLM-Based**: Uses Ollama as a local large language model backend for generating responses.
* **Async-First**: All operations are asynchronous and non-blocking.
* **Lightweight**: Stateless service optimized for high-concurrency chat tasks.

---

## 📁 Internal Structure

```text
chat
├── src
│   ├── __init__.py         # app package init
│   ├── chat.py             # core chat logic for generating responses
│   └── client.py           # ollama client setup
├── .python-version         # python version lock
├── broker.py               # message broker setup
├── config.py               # configuration loading
├── Dockerfile              # container image definition
├── main.py                 # entry point
├── pyproject.toml          # build system and dependencies
├── README.md               # documentation
└── uv.lock                 # `uv` dependency lock file
```

---

## 📝 Notes

* All communication is via RabbitMQ; no HTTP API is exposed directly.
* Designed to be plug-and-play with minimal configuration.
