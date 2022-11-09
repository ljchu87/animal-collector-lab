from django.contrib import admin
# import your models here
from .models import Animals, Feeding, Toy

# Register your models here
admin.site.register(Animals)
admin.site.register(Feeding)
admin.site.register(Toy)