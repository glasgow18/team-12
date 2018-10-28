from django.db import models

class Service(models.Model):

    name = models.CharField()
    location = models.CharField()
    gender = models.CharField()
    age = models.IntegerField()
    contact = models.CharField() # how user want to contact us
    interaction = models.CharField() # the way user want to interact with other ex. face to face, group call etc.
    symtoms = models.CharField()
    link = models.CharField()
    if_internal = models.CharField()


    @classmethod
    def create(cls, name,location,gender,age,contact,interaction,symtoms,link,if_internal):
        service = cls(name = name, location = location,  gender = gender, age = age, contact = contact, interaction = interaction, symtoms = symtoms, link = link, if_internal = if_internal)

        return service

service = Service.create("Pride and Prejudice")