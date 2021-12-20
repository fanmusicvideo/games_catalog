from django.contrib import admin
from .models import (
    Game, Rating, Genre,
    Publisher, Company, Developer,
    License, Award, Document
)


admin.site.register(Game)
admin.site.register(Document)
admin.site.register(Rating)
admin.site.register(Genre)
admin.site.register(Publisher)
admin.site.register(Company)
admin.site.register(Developer)
admin.site.register(License)
admin.site.register(Award)
