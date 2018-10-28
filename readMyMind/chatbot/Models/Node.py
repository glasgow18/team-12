from django.db import models

class Node(models.Model):

    title = models.CharField()
    prev_pointer = models.CharField()
    message = models.CharField()
    next_pointer = models.CharField()

    @classmethod
    def create(cls, title,prev_pointer,message,next_pointer):
        node = cls(title = title, prev_pointer = prev_pointer, message = message, next_pointer = next_pointer)

        return node

node = Node.create("Pride and Prejudice")