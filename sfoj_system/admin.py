from django.contrib import admin
from .models import Board, Judge_State, User_Table, Code_History

# Register your models here.
admin.site.register(Board)
admin.site.register(Judge_State)
admin.site.register(User_Table)
admin.site.register(Code_History)