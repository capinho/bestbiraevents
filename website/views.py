from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.views.generic import ListView,DetailView
from templated_email import send_templated_mail

import os



def HomeView(request):
    return render(request,'accueil.html')    


def about(request):
    return render(request,'about.html',{})

def tournage(request):
    return render(request, 'equipe-de-tournage-et-production-video.html')
    

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        send_templated_mail(
                template_name='welcome',
                from_email=email,
                recipient_list=['papadiawara@hotmail.fr'],
                context={
                    'name':name,
                    'message':message,
                },
                # Optional:
                # cc=['cc@example.com'],
                # bcc=['bcc@example.com'],
                # headers={'My-Custom-Header':'Custom Value'},
                # template_prefix="my_emails/",
                # template_suffix="email",
        )
        return render(request,'contact.html',{'name':name,'message':message,'email':email})    
    else:    
        return render(request,'contact.html',{})    


def services(request):
    return render(request,'production-video-corporative-et-entreprise.html',{})

def marketing(request):
    return render(request,'marketing-video-et-creation-de-contenu.html')
    
def pourquoiLaVideo(request):
    return render(request,'pourquoi-la-video-fonctionne-et-ses-benefices.html')

def processus(request):
    return render(request,'nos-processus-de-production-video.html')
    
def soumission(request):
    return render(request,'demande-de-soumission-video.html')

