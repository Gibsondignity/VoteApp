from django.contrib import admin

# Register your models here.
from .models import MovieTitle, Contestants, Nominations, Category

admin.site.register(MovieTitle)
admin.site.register(Category)
admin.site.register(Contestants)
admin.site.register(Nominations)
#admin.site.register(Votes)

