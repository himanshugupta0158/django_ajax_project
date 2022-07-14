from django.shortcuts import render

from app.models import Profile

from django.http import JsonResponse, HttpResponse
# Create your views here.


def index(request):
    return render(request, 'index.html')


def getProfiles(request):
    profiles = Profile.objects.all().order_by('-id')
    return JsonResponse({"profiles" : list(profiles.values())})


def create(request):
    if request.method == 'POST' :
        name = request.POST['name']
        email = request.POST['email']
        bio = request.POST['bio']
        new_profile = Profile(name=name,email=email,bio=bio)
        new_profile.save()
        print(new_profile)

        return HttpResponse("New Profile Created Successfully.")

