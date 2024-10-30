from typing import Any, Dict, Protocol, List

from app.mailing.service.tasks_service import TasksService

from app.mailing.schema.messenger import MessengerSchema
from app.mailing.models import Mailing, Recipients, Messengers, Accounts


class MailingMakerProtocol(Protocol):
    async def mailing(self, mailing:Mailing, accounts_numbers:List[str], recipients_numbers:List[str]) -> Any:...


class MessendgerManager(MailingMakerProtocol):

    def __init__(self, messenger_mailings_managers:Dict[str:MailingMakerProtocol]):

        self.messenger_mailings_managers = messenger_mailings_managers


    def create_messengers_models(self):
        for name in self.messenger_mailings_managers.keys():
            messenger = MessengerSchema(messenger_name=name)
            if(self.messengers_repository.is_exists(messenger)):
                self.messengers_repository.create(messenger)

    async def mailing(self, schema:Mailing) -> Any:

        messengers_names = [messenger.name for messenger in schema.messengers]

        for messenger_name in messengers_names:

            accounts_numbers = self.accounts_repository.get_all_in(messenger_name)
            recipients_numbers = self.recipients_repository.get_all_in(messenger_name)

            messenger_client = self.messenger_mailings_managers.get(messenger_name.upper())
            if(messenger_client):
                try:
                    self.tasks_service.start_new_task(messenger_client.mailing(schema, accounts_numbers, recipients_numbers))
                except Exception as e:
                    raise Exception("Start task exception")
                
            else:
                raise Exception("Messenger client not initialized")

