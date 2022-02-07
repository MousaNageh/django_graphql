
from django.contrib import admin
from .models import Books,Category,Question,Quiz,Answer
# Register your models here.
admin.site.register([Books,Category,Question,Quiz,Answer])
