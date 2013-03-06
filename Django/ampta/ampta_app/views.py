# Create your views here.
from django.shortcuts import get_list_or_404, render, redirect, get_object_or_404
from django.http import HttpResponse
#from django.template import Context, loader

from ampta_app.models import Project, ProjectForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required

###
#Login
###

def login_user(request):
	message = ''
	if request.method == "POST":

		form = LoginForm(request.POST)
		if form.is_valid():
			username_to_try = form.cleaned_data["username"]
			password_to_try = form.cleaned_data["password"]

			user = authenticate(username=username_to_try, password=password_to_try)
			if user is not None:
				if user.is_active:
					login(request, user)
					request.session['has_logged_in'] = True
					return redirect('/projects/')
				else:
					return HttpResponse("<h1>Funkar inte</h1>")
			else:
				message = "Fel anvandarnamn eller losenord"
	else:
		form = LoginForm()
	return render(request, 'login.html' ,{'form' : form, 'message' : message})

###
#Logout
###
def logout_user(request):
	#avsluta sessionen
	logout(request)
	return redirect('/login/')

##
#Project
##

def project_list(request):
	projects = get_list_or_404(Project.objects.order_by('project_name'))
	return render(request, 'projects/list.html', {"projects" : projects})

@permission_required('ampta_app.can_add_project', login_url='/permission/error/')
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

@login_required(login_url='/login/')
def project_show(request, project_id):
	project = get_object_or_404(Project, pk=project_id)
	return render(request, 'projects/show.html', {'project': project})
	
def project_delete(request, project_id):
	project = get_object_or_404(Project, pk=project_id)
	if project.owned_by_user(request.user):
		project.delete()
		return redirect('/projects/')
	else:
		return HttpResponse("Du har ej rattigheter att ta bort projekt")

@login_required(login_url='/login')
def project_edit(request, project_id):
	project = get_object_or_404(Project, pk=project_id)
	if project.owned_by_user(request.user):
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

###
#Sidebar
###
def sidebar(request):
	#kommer at den inloggade anvandaren
	user = request.user
	projects = User.object.filter(owner = user)
	return render(request, 'shared/base.html', {"projects" : projects,})

###
#Error
###

def error_permission(request):
	return HttpResponse("Du har ej rattigheter") 









