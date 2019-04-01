from django.contrib import admin
from .models import Boards, Lists, Cards, Labels

# Register your models here.
admin.site.register(Boards)
admin.site.register(Lists)
admin.site.register(Cards)
admin.site.register(Labels)
