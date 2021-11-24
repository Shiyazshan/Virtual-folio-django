from django.shortcuts import render
from works.models import Project,Service


def index(request):
    project = Project.objects.all()
    service = Service.objects.all()

    context = {
        "project" : project,
        "service" : service,
    }
    return render(request,"index.html",context=context)

