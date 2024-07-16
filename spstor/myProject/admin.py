from django.contrib import admin

# Register your models here.

from .models import User,Game,Library,Categorie

admin.site.register(User)
admin.site.register(Game)
admin.site.register(Library)
admin.site.register(Categorie)

