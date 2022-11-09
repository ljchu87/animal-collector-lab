from django.contrib import admin
# import your models here
from .models import Animals, Feeding

# Register your models here
admin.site.register(Animals)
admin.site.register(Feeding)