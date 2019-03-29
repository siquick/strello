from django.contrib import admin
from .models import Boards, Lists, Cards

# Register your models here.
admin.site.register(Boards)
admin.site.register(Lists)
admin.site.register(Cards)