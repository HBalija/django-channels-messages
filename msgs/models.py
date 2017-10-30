from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.humanize.templatetags.humanize import naturaltime
from django.conf import settings


class User(AbstractUser):

    AbstractUser._meta.get_field('email')._unique = True


class Message(models.Model):

    user = models.ForeignKey(User, related_name="user")
    message = models.TextField(max_length=500, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        # change to -timestamp for ajax implement
        ordering = ['timestamp']

    def __str__(self):
        return '{} {}'.format(self.user, self.id)

    @property
    def message_data(self):
        """
        Data sent by channels for a new message.
        """
        data = {
            'message': self.message,
            'formated': naturaltime(self.message),
            'timestamp': str(self.timestamp),
            'author': self.message_author.username,
            'id': self.id,
        }

        return data

    @classmethod
    def get_messages(cls, mess_id=None):

        q = cls.objects.all()

        # last number of messages in reversed order
        if mess_id:
            q = q.filter(id__lt=int(mess_id))

        q = q[:settings.DEFAULT_NUMBER_OF_MESSAGES]

        for message in q:
            message.timestamp_formatted = str(message.timestamp)

        return q[::-1]
