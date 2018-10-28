from django.db import models

class Contact(models.Model):

    id = models.CharField()
    name = models.CharField()
    email = models.CharField()
    phone = models.CharField()

    @classmethod
    def create(cls, id,name,email,phone):
        contact = cls(id = id,name = name,email = email, phone = phone)

        return contact

contact = Contact.create("Pride and Prejudice")