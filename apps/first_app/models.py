from __future__ import unicode_literals
from django.db import models

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}

        # Validations for the username
        if len(postData['username']) < 3:
            errors['length'] = 'Username must be greater than 3 characters'
        
        # Validations for the email
        email = postData['email']
        if '@' not in email:
            errors['email'] = "Invalid email"
        if '.' not in email:
            errors['email'] = "Invalid email"

        # Valitdations for the password
        if len(postData['password']) < 8:
            errors['password'] = "Password must be greater than 7 characters"
        return errors

class DogManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}

        # Validations for the username
        if len(postData['breed']) < 3:
            errors['breed'] = 'Invalid dog breed.'

        if len(postData['bio']) < 1:
            errors['bio'] = 'Must enter a bio.'
        return errors



class User(models.Model):
    username = models.CharField(max_length = 15)
    email = models.CharField(max_length = 50)
    password = models.CharField(max_length = 25)
    objects = UserManager()


class Dog(models.Model):
    dog_name = models.CharField(max_length = 25)
    dog_size = models.CharField(max_length = 25)
    breed = models.CharField(max_length = 25)
    bio = models.CharField(max_length = 225)
    image = models.ImageField(default='default.png', blank = True)
    dog_owner = models.ForeignKey(User, related_name='my_dogs', on_delete = models.CASCADE)
    objects = DogManager()

class Like(models.Model):
    dog_liked = models.ForeignKey(Dog, related_name='likes', on_delete = models.CASCADE)
    liker = models.ForeignKey(Dog, related_name='the_likes', on_delete = models.CASCADE)


