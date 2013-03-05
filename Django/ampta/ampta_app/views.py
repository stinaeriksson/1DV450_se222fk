# Create your views here.
from django.shortcuts import get_list_or_404, render
#from django.http import HttpResponse
#from django.template import Context, loader

from ampta_app.models import Project

def project_list(request):
	projects = get_list_or_404(Project.objects.order_by('project_name'))
	return render(request, 'projects/list.html', {"projects" : projects})

