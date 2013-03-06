# Create your views here.
from django.shortcuts import get_list_or_404, render, redirect, get_object_or_404
#from django.http import HttpResponse
#from django.template import Context, loader

from ampta_app.models import Project, ProjectForm

def project_list(request):
	projects = get_list_or_404(Project.objects.order_by('project_name'))
	return render(request, 'projects/list.html', {"projects" : projects})

def project_add(request):
	if request.method == "POST":
		form = ProjectForm(request.POST)
		if form.is_valid():
			#form.instance.owner = request.user
			try:
				form.save()
				return redirect(project_list)
			except:
				return HttpResponseServerError()
	else:
		form = ProjectForm()

	return render(request, 'projects/add.html', {"form": form})

def project_show(request, project_id):
	project = get_object_or_404(Project, pk=project_id)
	return render(request, 'projects/show.html', {'project': project})
	
def project_delete(request, project_id):
	project = get_object_or_404(Project, pk=project_id)
	project.delete()
	return redirect('/projects/')

def project_edit(request, project_id):
	project = get_object_or_404(Project, pk=project_id)
	if request.method == "POST":
		form = ProjectForm(request.POST, instance = project)
		if form.is_valid():
			try:
				form.save()
				return redirect(project_list)
			except:
				return HttpResponseServerError()
	else:
		form = ProjectForm(instance = project)

	return render(request, 'projects/edit.html', {"form": form, "project" : project,})







