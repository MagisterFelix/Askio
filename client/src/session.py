from uuid import UUID

from gradio.components.chatbot import Message, MessageDict


class Session:
    _id: UUID | None = None
    _messages: list[MessageDict | Message] = []

    def get_id(self) -> UUID | None:
        return self._id

    def set_id(self, new_id: UUID | None) -> None:
        self._id = new_id

    def clear_id(self) -> None:
        self._id = None

    def get_messages(self) -> list[MessageDict | Message]:
        return self._messages

    def set_messages(self, messages: list[MessageDict | Message]) -> None:
        self._messages = messages

    def add_messages(self, messages: list[MessageDict | Message]) -> None:
        self._messages.extend(messages)

    def clear_messages(self) -> None:
        self._messages.clear()

    def clear_data(self) -> None:
        self.clear_id()
        self.clear_messages()


session = Session()
