from __future__ import unicode_literals
from django.db import models
from apps.first_app.models import *

class MessageManager(models.Manager):
  def basic_validator(self, postData):
    errors = {}

    # Validations for the message
    if len(postData['message']) < 1:
      errors['length'] = 'No message to send.'
    
    return errors

class Message(models.Model):
  message = models.CharField(max_length = 225)
  user_message = models.ForeignKey(User, related_name = 'my_messages', on_delete = models.CASCADE)
  objects = MessageManager()

