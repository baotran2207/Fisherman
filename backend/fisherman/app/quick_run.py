# This file is for quick and dirty implement patterns
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Callable, Protocol


class MailProvider(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def send(self, msg):
        pass


class SMTPProvider(MailProvider):
    def send(self, msg):
        print(f"Send with SMTP {msg}")

    def connect(self):
        print("connected SMTP")


class SESProvider(MailProvider):
    def send(self, msg):
        print(f"send with ses {msg}")


@dataclass
class MailSender:
    provider: MailProvider = SMTPProvider

    def set_provider(self, new_provider: MailProvider):
        self.provider = new_provider

    def send_email(self, message: str) -> None:
        self.provider.connect()
        self.provider.send(message)


def send_email() -> None:

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
