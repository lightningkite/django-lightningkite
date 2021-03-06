from .channel import Channel
from django.db import models
from ..signals import sending, sent


class DatabaseChannel(Channel):

    def send(notifiable, notification, *args, **kwargs):
        """
        Send the Given Notifiction
        """

        message = notification.to_db(notifiable, *args, **kwargs)

        if isinstance(message, models.Model):
            sending.send(sender=DatabaseChannel, notifiable=notifiable, notification=notification)
            try:
                message.save()
                sent.send(sender=DatabaseChannel, notifiable=notifiable, notification=notification)
            except Exception as e:
                raise e
