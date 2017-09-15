from django.db import models

# Create your models here.

class Recipient(models.Model):
    email = models.EmailField(help_text="Upon hitting contact me on the main page, will send an email to all emails listed here.")

    def __str__(self):
        return self.email
