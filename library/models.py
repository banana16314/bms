from django.db import models


class Book(models.Model):
    isbn = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author')
    editor = models.ForeignKey('Editor')
    press = models.ForeignKey('Press')
    bookstore = models.ForeignKey('Bookstore')

    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    college = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Press(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    street = models.CharField(max_length=200)

    def __str__(self):
        return self.name



class Editor(models.Model):
    name = models.CharField(max_length=200)
    press = models.ForeignKey('Press')
    author = models.ForeignKey('Author')

    def __str__(self):
        return self.name


class Bookstore(models.Model):
    name = models.CharField(max_length=200)
    website = models.URLField()

    def __str__(self):
        return self.name
