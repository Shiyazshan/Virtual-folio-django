from django.contrib import admin
from users.models import Profile,Address,Education,Experience,Skill


class ProfileAdmin(admin.ModelAdmin):
    list_display = ["id", "image", "name", "designation", "address", "description", "age", "gender", "resume"]
admin.site.register(Profile)

admin.site.register(Address)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Skill)
