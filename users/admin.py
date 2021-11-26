from django.contrib import admin
from users.models import Profile,Address,Education,Experience,Skill


admin.site.register(Profile)
admin.site.register(Address)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Skill)
