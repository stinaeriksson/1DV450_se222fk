# -*- coding: utf-8 -*-
from django.shortcuts import get_list_or_404, render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseServerError


from ampta_app.models import Project, Ticket
from ampta_app.forms import TicketForm, ProjectForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages


def index(request):
	return render(request, 'index.html')

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
					return redirect(index)
				else:
					return HttpResponse("<h1>Funkar inte</h1>")
			else:
				message = "Fel användarnamn eller lösenord"
	else:
		form = LoginForm()
	return render(request, 'login.html' ,{'form' : form, 'message' : message})

###
#Logout
###
def logout_user(request):
	#avsluta sessionen
	logout(request)
	return redirect(login_user)

##
#Project
##
@login_required(login_url='/login')
def project_list(request):
	projects = get_list_or_404(Project.objects.order_by('project_name'))
	return render(request, 'projects/list.html', {"projects" : projects})


@login_required(login_url='/login')
@permission_required('ampta_app.can_add_project', login_url='/index/')
def project_add(request):
	if request.method == "POST":
		form = ProjectForm(request.POST)
		if form.is_valid():
			form.instance.owner = request.user
			try:
				project = form.save()
				request.flash['notice'] = 'Projektet sparat!'
				return redirect(project_show, project.pk)
			except:
				return HttpResponseServerError()
	else:
		form = ProjectForm()

	return render(request, 'projects/add.html', {"form": form})

@login_required(login_url='/login/')
def project_show(request, project_id):
	project = get_object_or_404(Project, pk=project_id)
	if not (project.user_in_project(request.user) or project.owned_by_user(request.user)):	
		return redirect(project_list)


	else:
		return render(request, 'projects/show.html', {'project': project})

	

@login_required(login_url='/login')
def project_delete(request, project_id):
	project = get_object_or_404(Project, pk=project_id)
	if project.owned_by_user(request.user):
		project.delete()
		request.flash['notice'] = 'Projektet borttaget!'
		return redirect('/projects/')
	else:
		request.flash['error'] = 'Du har ej rättigheter att ta bort projektet'
		return redirect(index)

@login_required(login_url='/login')
def project_confirm_delete(request, project_id):
	project = get_object_or_404(Project, pk=project_id)
	if not project.owned_by_user(request.user):
		request.flash['error'] = 'Du har ej rättigheter att ta bort projektet'
		return redirect(index)
	return render(request, 'projects/confirm_delete.html', {'project': project, 'message': 'Är du säker på att du vill ta bort projektet'})

@login_required(login_url='/login')
def project_edit(request, project_id):
	project = get_object_or_404(Project, pk=project_id)

	if not project.owned_by_user(request.user):
		request.flash['error'] = 'Du har ej rättigheter att editera projektet'
		return redirect(index)

	if request.method == "POST":
		form = ProjectForm(request.POST, instance = project)
		if form.is_valid():
			try:
				form.save()
				request.flash['notice'] = 'Projektet uppdaterat!'
				return redirect(project_show, project.pk)
			except:
				return HttpResponseServerError()
	else:
		form = ProjectForm(instance = project)


	return render(request, 'projects/edit.html', {"form": form, "project" : project,})

@login_required(login_url='/login')
def project_filter(request):
	projects = get_list_or_404(Project.objects.order_by('project_name'))
	return render(request, 'projects/filter.html', {"projects" : projects})


###
#Tickets
###
@login_required(login_url='/login')
def ticket_add(request, project_id):
	project = get_object_or_404(Project, pk=project_id)
	if not (project.user_in_project(request.user) or project.owned_by_user(request.user)):	
		request.flash['error'] = 'Du har ej rättigheter att lägga till ticket till detta projekt'
		return redirect(index)

	if request.method == "POST":
		form = TicketForm(request.POST)
		if form.is_valid():
			form.instance.project = project
			form.instance.user = request.user
			try:
				ticket = form.save()
				request.flash['notice'] = 'Ticket sparad!'
				return redirect(ticket_show, ticket.pk)
			except:
				return HttpResponseServerError()
	else:
		form = TicketForm()

	return render(request, 'tickets/add.html', {"form": form})

@login_required(login_url='/login/')
def ticket_show(request, ticket_id):
	ticket = get_object_or_404(Ticket, pk=ticket_id)
	if not (ticket.owned_by_user(request.user) or ticket.is_project_owner(request.user)):	
		request.flash['error'] = 'Du har ej rättigheter att se ticket'
		return redirect(index)
	return render(request, 'tickets/show.html', {'ticket': ticket})

@login_required(login_url='/login')
def ticket_delete(request, ticket_id):
	ticket = get_object_or_404(Ticket, pk=ticket_id)
	if not (ticket.owned_by_user(request.user) or ticket.is_project_owner(request.user)):	
		request.flash['error'] = 'Du har ej rättigheter att ta bort ticket'
		return redirect(index)
	project_id = ticket.project.id
	ticket.delete()
	request.flash['notice'] = 'Ticket borttagen!'
	return redirect(project_show, project_id)
	

@login_required(login_url='/login')
def ticket_confirm_delete(request, ticket_id):
	ticket = get_object_or_404(Ticket, pk=ticket_id)
	if not (ticket.owned_by_user(request.user) or ticket.is_project_owner(request.user)):	
		request.flash['error'] = 'Du har ej rättigheter att ta bort ticket'
		return redirect(index)
	return render(request, 'tickets/confirm_delete.html', {'ticket': ticket, 'message': 'Är du säker på att du vill ta bort ticket'})

@login_required(login_url='/login')
def ticket_edit(request, ticket_id):
	ticket = get_object_or_404(Ticket, pk=ticket_id)
	if not (ticket.owned_by_user(request.user) or ticket.is_project_owner(request.user)):	
		request.flash['error'] = 'Du har ej rättigheter att editera ticket'
		return redirect(index)

	if request.method == "POST":
		form = TicketForm(request.POST, instance = ticket)
		if form.is_valid():
			try:
				ticket = form.save()
				request.flash['notice'] = 'Ticket uppdaterad!'
				return redirect(ticket_show, ticket.pk)
			except:
				return HttpResponseServerError()
	else:
		form = TicketForm(instance = ticket)

	return render(request, 'tickets/edit.html', {"form": form, "ticket" : ticket,})



def User(request):
	if request.user.is_anonymous():
		return redirect(login_user)
	else:
		user = request.user
		user_projects = user.projects.all()
		user_tickets = user.tickets.all()
		
		return {'user':user, 'user_projects':user_projects, 'user_tickets':user_tickets, }
	







