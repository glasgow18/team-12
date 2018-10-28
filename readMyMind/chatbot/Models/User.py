from django.db import models

class User(models.Model):

    id = models.CharField()
    name = models.CharField()
    age = models.IntegerField()
    location = models.CharField()
    gender = models.CharField()

    @classmethod
    def create(cls, id,name,age,location,gender):
        user = cls(id = id,name = name, age = age, location = location, gender = gender)

        return user

user = User.create("Pride and Prejudice")