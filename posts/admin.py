from django.contrib import admin
from .models import Posts

# Register your models here.
admin.site.site_header = "Welcome to Blog Admin"
admin.site.register(Posts)
