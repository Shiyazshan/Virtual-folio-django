# default
import json
from django.shortcuts import render
from django.http.response import HttpResponse
from users.models import Clients, Profile,Address,Education,Experience,Skill
from web.models import Subscribe,Testimonial,Contact
from works.models import Service, Project


def index(request):
    profile = Profile.objects.get(user_id=1)
    skills = Skill.objects.filter(user_id=profile.pk)
    education = Education.objects.all()
    experience = Experience.objects.all()
    service = Service.objects.all()
    project = Project.objects.all()
    testimonial = Testimonial.objects.all()
    total_clients = Clients.objects.all().count()
    completed_project_count = project.filter(is_completed=True).count()
    satisfied_clients_count = project.filter(is_satisfied=True).count()
    pending_projects_count = project.count() - completed_project_count


    context = {
        'profile' : profile,
        'skills' : skills,
        'education' : education,
        'experience' : experience,
        'service' : service,
        'project' : project,
        'testimonial' : testimonial,
        'total_clients' : total_clients,
        'satisfied_clients_count' : satisfied_clients_count,
        'pending_projects_count' : pending_projects_count,
    }

    return render(request, "index.html",context = context)


def subscribe(request):
    email = request.POST.get("email")

    if not Subscribe.objects.filter(email=email).exists():
        Subscribe.objects.create(
            email = email
        )

        response_data = {
            "status" :"success",
            "message" : "You subscribed to our newsletter successfully",
            "title" : "Successfully Registered"
        }
    else:
        response_data = {
            "status" :"warning",
            "message" : "You are already a member. No need to register again",
            "title" : "You are already subscribed."
        }

    return HttpResponse(json.dumps(response_data),content_type="application/javascript")
