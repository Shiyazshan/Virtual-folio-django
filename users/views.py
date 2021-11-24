from django.shortcuts import render
from users.models import Profile,Address,Education,Experience,Skill,SkillItem


def index(request):
    profile = Profile.objects.all()
    address = Address.objects.all()
    education = Education.objects.all()
    experience = Experience.objects.all()
    skill = Skill.objects.all()
    skillitem = SkillItem.objects.all()


    context = {
        "profile" : profile,
        "address" : address,
        "education" : education,
        "experience" : experience,
        "skill" : skill,
        "skillitem" : skillitem,

    }
    return render(request, "index.html",context = context)