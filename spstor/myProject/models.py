from django.db import models

class User(models.Model):
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.login


class Categorie(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(blank=True ,upload_to='images')

    def __str__(self):
        return self.name

class Game(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    price = models.FloatField()
    short_text = models.TextField()
    image = models.ImageField(blank=True, upload_to='images')

    def __str__(self):
        return self.name

class Library(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        return self.user