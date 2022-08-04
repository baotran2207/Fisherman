# This file is for quick and dirty implement patterns
from abc import ABC, abstractmethod
from asyncio import protocols
from dataclasses import dataclass
from typing import Callable, Protocol, List
from xmlrpc.client import boolean


class MailProvider(Protocol):
    @abstractmethod
    def connect(self) -> str:
        pass

    @abstractmethod
    def send(self, msg) -> str:
        pass


class SMTPProvider:
    def send(self, msg) -> str:
        return f"Send with SMTP {msg}"

    def connect(self):
        return f"connected SMTP"


class SESProvider:
    def send(self, msg):
        return (f"send with ses {msg}")

    def connect(self) -> List:
        return ('connect sqs')


class MailSender:
    provider: MailProvider = SMTPProvider

    def set_provider(self, new_provider: MailProvider):
        self.provider = new_provider

    def send_email(self, message: str) -> None:
        self.provider.connect()
        self.provider.send(message)


def send_email() -> None:

    int

    settings_email_sender_type = "SMTP"
    messsage = "Test message "
    mail_provider = SMTPProvider()
    mail_provider_sqs = SESProvider()
    sender = MailSender(mail_provider)

    sender.send_email(messsage)

    sender.set_provider(mail_provider_sqs)

    sender.send_email(messsage)


if __name__ == "__main__":
    send_email()
