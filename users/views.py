from django.shortcuts import render
from users.models import Profile,Address,Education,Experience,Skill,SkillItem


def index(request):
    address = Address.objects.all()
    education = Education.objects.all()
    experience = Experience.objects.all()
    skill = Skill.objects.all()
    skillitem = SkillItem.objects.all()
    profile = Profile.objects.all()


    context = {
        "address" : address,
        "education" : education,
        "experience" : experience,
        "skill" : skill,
        "skillitem" : skillitem,
        "profile" : profile,

    }
    return render(request, "index.html",context = context)


def profile(request,pk):
    profile = Profile.objects.get(pk=pk)[:2]

    context = {
        "profile" : profile
    }
    return render(request,"index.html",context=context)