from django.db import models

import django.utils.timezone

class Contact(models.Model):
    name = models.CharField(max_length=50, verbose_name='name')
    email = models.EmailField(max_length=50, verbose_name='email')
    subject = models.CharField(max_length=150, verbose_name='subject')
    message = models.TextField(max_length=5000, verbose_name='message')
    message_received_datetime = models.DateTimeField(default=django.utils.timezone.now, verbose_name='message received datetime')
    user_id = models.BigIntegerField(null=True, default=None, blank=True, verbose_name='user Id')

    class Meta:
        db_table = 'contact'

    def __str__(self):
        return self.email