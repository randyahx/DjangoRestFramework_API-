from django.db import models


# class Accounts(models.Model):
#     created = models.DateTimeField(auto_now_add=True)
#     username = models.CharField(max_length=20, default='')
#     password = models.CharField(max_length=20, default='')
#     admin = models.BooleanField(default=False)
#
#     class Meta:
#         ordering = ['username']


class Messages(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=100, default='')
    owner = models.ForeignKey('auth.User', related_name='Messages', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']

    
