from django.db import models

class Contact(models.Model):

    name = models.CharField(max_length=120)
    email = models.EmailField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.name