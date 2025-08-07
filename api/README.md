# 🌐 API

The `API` exposes a public-facing asynchronous HTTP API using **FastAPI**. It serves as the main entry point for external clients and communicates with internal services through **RabbitMQ** via **FastStream**.

---

## 🧠 Responsibilities

* Provide async HTTP endpoints for clients
* Validate and route incoming requests
* Publish requests to the message broker (RabbitMQ)
* Optionally receive and forward responses/events from other components

---

## ⚙️ Technologies

| Layer         | Tool                          |
| ------------- | ----------------------------- |
| Web Framework | FastAPI                       |
| Data Models   | Pydantic                      |
| Messaging     | FastStream \[RabbitMQ]        |
| Configuration | Pydantic \[pydantic-settings] |
| Async Runtime | Python asyncio                |

---

## 🏗️ Architecture

* **Async API**: Built with FastAPI and fully asynchronous I/O.
* **Event-Based Backend**: Publishes user actions as events to RabbitMQ.
* **Decoupled**: Does not process business logic directly — acts as a gateway layer.
* **Extensible**: Modular views and model definitions for clean routing and validation.

---

## 📁 Internal Structure

```text
api
├── src
│   ├── models
│   │   ├── __init__.py       # model package init
│   │   ├── message.py        # message model definition
│   │   └── response.py       # response model definition
│   ├── views
│   │   ├── __init__.py       # view package init
│   │   └── message.py        # API endpoints for message handling
│   ├── __init__.py           # app package init
│   └── core.py               # app setup and routing
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

* All routes and message handling are asynchronous.
* Uses `Pydantic` for request validation and response serialization.
* Message broker integration enables scalable and decoupled communication with internal services.
