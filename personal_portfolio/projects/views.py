from django.shortcuts import render
from projects.models import Projects
# Create your views here.
def project_index(request):
    projects = Projects.objects.all() # Performing a ORM query
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)
