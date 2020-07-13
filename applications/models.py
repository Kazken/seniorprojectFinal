from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=20)
    RoleID = models.IntegerField(null=False)
    Apps = models.ManyToManyField('Apps', blank=False)

    def _str_(self):
        return self.name

class Apps(models.Model):
    name = models.CharField(max_length=25)

    def _str_(self):
        return self.name


class RoleList(models.Model):
    name = models.CharField(max_length=25)
