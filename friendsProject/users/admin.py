from django.contrib import admin
from .models import Profile

# Register your models here.
# superuser: user-admin password-superuser123
admin.site.register(Profile)
