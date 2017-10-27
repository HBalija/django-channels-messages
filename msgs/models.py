from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.humanize.templatetags.humanize import naturaltime


class User(AbstractUser):

    AbstractUser._meta.get_field('email')._unique = True


class Message(models.Model):

    user = models.ForeignKey(User, related_name="user")
    content = models.TextField(max_length=500, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return '{} {}'.format(self.user, self.id)

    @property
    def message_data(self):
        """
        Data sent by channels for a new message.
        """
        data = {
            'message': self.content,
            'formated': naturaltime(self.content),
            'timestamp': str(self.timestamp),
            'author': self.message_author.username,
            'id': self.id,
        }

        return data
