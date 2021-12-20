from django.db import models


class Document(models.Model):
    upload = models.FileField(upload_to='uploads/%Y.%m.%d/')

    def __str__(self):
        return str(self.upload)


class Game(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    rating = models.ForeignKey('Rating', on_delete=models.CASCADE)
    genres = models.ManyToManyField('Genre')
    publishers = models.ManyToManyField('Publisher')
    developers = models.ManyToManyField('Developer')
    companies = models.ManyToManyField('Company')
    awards = models.ManyToManyField('Award')
    licenses = models.ManyToManyField('License')

    def __str__(self):
        return self.title


class Publisher(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()

    def __str__(self):
        return self.name


class License(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()

    def __str__(self):
        return self.name


class Award(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()

    def __str__(self):
        return self.name


class Developer(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()

    def __str__(self):
        return self.name


class Rating(models.Model):
    name = models.CharField(max_length=3)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name
