from django.contrib import admin
from .models import Empolly,Department,Role

# Register your models here.
admin.site.register(Department)
admin.site.register(Empolly)
admin.site.register(Role)
