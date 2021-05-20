from django.apps import AppConfig
# импорт класса Signal и метода send_activation_notification для отправки сообщения об активации пользователю
# import of the Signal class and the send_activation_notification method to send an activation message to the user
from django.dispatch import Signal
from .utilities import send_activation_notification


user_registered = Signal(providing_args=['instance'])


def user_registered_dispatcher(sender, **kwargs):
    send_activation_notification(kwargs['instance'])


user_registered.connect(user_registered_dispatcher)


class AccountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'account'
