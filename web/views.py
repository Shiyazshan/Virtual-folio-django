# default
import json
import os
from types import ClassMethodDescriptorType

from django.shortcuts import render
from django.http.response import HttpResponse,Http404
from django.conf import settings

from users.models import Client, Profile,Address,Education,Experience,Skill, SkillItem,Client
from web.models import Subscribe,Testimonial,Contact
from works.models import Service, Project


def index(request):
    profile = Profile.objects.get(user_id=1)
    skills = Skill.objects.filter(user_id=profile.pk)
    skill_items = SkillItem.objects.filter(skill__user_id=profile.pk)
    education = Education.objects.all()
    experiences = Experience.objects.all()
    services = Service.objects.all()
    project = Project.objects.all()
    testimonial = Testimonial.objects.all()
    total_clients = Client.objects.all().count()
    completed_project_count = project.filter(is_completed=True).count()
    satisfied_clients_count = project.filter(is_satisfied=True).count()
    pending_projects_count = project.count() - completed_project_count
    contact = Contact.objects.all()
    address = Address.objects.all()
    category = Project.objects.all()
    clients = Client.objects.all()

    context = {
        'profile' : profile,
        'skills' : skills,
        'skill_items' : skill_items,
        'education' : education,
        'experiences' : experiences,
        'services' : services,
        'project' : project,
        'testimonial' : testimonial,
        'total_clients' : total_clients,
        'satisfied_clients_count' : satisfied_clients_count,
        'pending_projects_count' : pending_projects_count,
        'completed_project_count' : completed_project_count,
        'contact' : contact,
        'address' : address,
        'category' : category,
        'clients' : clients
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


def contact(request):
    email = request.POST.get("email")
    name = request.POST.get("name")
    subject = request.POST.get("subject")
    message = request.POST.get("message")

    if not Contact.objects.filter(email=email).exists():

        Contact.objects.create(
            email = email,
            name = name,
            subject = subject,
            message = message,
        )
        response_data = {
            "status" :"success",
            "message" : "Your message has been successfully sent. We will contact you very soon!",
            "title" : "Thank you for contacting us"
        }
    else:
        response_data = {
            "status" :"warning",
            "message" : "This email address is already being used",
            "title" : "Add another email address that you own"
        }
    return HttpResponse(json.dumps(response_data),content_type="application/javascript")


def download(request,path):
    file_path=os.path.join(settings.MEDIA_ROOT,path)

    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response=HttpResponse(fh.read(),content_type="application/adminupload")
            response['Content-Disposition']='inline;filename='+os.path.basename(file_path)

            return response
    
    raise Http404

