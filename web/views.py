# default
import json
from django.shortcuts import render
from django.http.response import HttpResponse
from web.models import Subscribe,Testimonial,Contact


def index(request):
    testimonials = Testimonial.objects.all()
    contacts = Contact.objects.all()

    context = {
        "testimonials" : testimonials,
        "contacts" : contacts
    }

    return render(request, "index.html", context = context)


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
