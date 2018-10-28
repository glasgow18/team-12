from django.db import models

class Symtomps(models.Model):

    name = models.CharField()
    synonyms = models.CharField()

    @classmethod
    def create(cls,name,synonyms):
        symtoms = cls(name = name, synonyms = synonyms)

        return symtoms

symtoms = Symtomps.create("Pride and Prejudice")