from django.contrib import admin
from testapp.models import GroupModel,TaskAssignModel

# Register your models here.

class GroupAdmin(admin.ModelAdmin):
	list_display = ['id','member','group','created_by']

class TaskAssignAdmin(admin.ModelAdmin):
	list_display = ['assigned_to','task','assigned_by']





admin.site.register(GroupModel,GroupAdmin)

admin.site.register(TaskAssignModel,TaskAssignAdmin)






