from django.db import models


class User(models.Model):
    STATUS = (
             ('Active', 'Active'),
             ('Inactive', 'Inactive'),
             )
    name = models.CharField(max_length=20, null=True)
    uname = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=20, null=True, choices=STATUS)
    role_id = models.IntegerField(null=False)
    #app_list = models.ManyToManyField('App', blank=False)

    def __str__(self):
        return self.name


class App(models.Model):
    STATUS = (
                 ('Active', 'Active'),
                 ('Inactive', 'Inactive'),
                 )
    name = models.CharField(max_length=25)
    user = models.ManyToManyField('User', blank=False)
    status = models.CharField(max_length=20, null=True, choices=STATUS)

    def __str__(self):
        return self.name


class RoleList(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
            return self.name
