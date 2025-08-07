# 🧑‍💻 Client

The `client` provides a user-facing interface using **Gradio** for interactive chat. It acts as a frontend that sends requests to the `API` via HTTP using the `requests` library.

---

## 🧠 Responsibilities

* Provide a web-based UI for end-users
* Collect user input and send it to the API component
* Display responses returned by the backend
* Maintain simple session

---

## ⚙️ Technologies

| Layer         | Tool                          |
| ------------- | ----------------------------- |
| UI Framework  | Gradio                        |
| HTTP Client   | Requests                      |
| Configuration | Pydantic \[pydantic-settings] |
| Runtime       | Python standard               |

---

## 🏗️ Architecture

* **Web UI**: Built with Gradio to allow chat input/output in a browser.
* **API Consumer**: Sends user messages to the `API` using HTTP.
* **Stateless Requests**: Each message is sent as a standalone request, with optional session tracking.
* **Simple UX**: Designed for quick lightweight interaction.

---

## 📁 Internal Structure

```text
client
├── src
│   ├── __init__.py         # app package init
│   ├── api.py              # handles HTTP requests to the API backend
│   ├── chat.py             # gradio logic and callbacks for chat interactions
│   └── session.py          # simple session tracking logic
├── .python-version         # python version lock
├── config.py               # configuration loading
├── Dockerfile              # container image definition
├── main.py                 # entry point
├── pyproject.toml          # build system and dependencies
├── README.md               # documentation
└── uv.lock                 # `uv` dependency lock file
```

---

## 📝 Notes

* Gradio auto-launches a browser window by default.
* Uses synchronous HTTP requests via `requests` (no broker or async backend).
* Minimal configuration needed.
