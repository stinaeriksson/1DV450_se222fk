from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import iri_to_uri
from django.forms import ModelForm
from django.forms.extras.widgets import SelectDateWidget
from django import forms

class Project(models.Model):
	project_name = models.CharField(max_length = 40)
	description = models.TextField()
	start_date = models.DateField()
	end_date = models.DateField()
	owner = models.ForeignKey(User, related_name="projects")
	users = models.ManyToManyField(User, related_name="projects_user")

	def __unicode__(self):
		return self.project_name

	def owned_by_user(self, user):
		return self.owner == user

	class Meta:
		permissions = (
			("can_add_project", "Can add project"),
		)

class Status(models.Model):
	status_name = models.CharField(max_length = 20)
	
	def __unicode__(self):
		return self.status_name

class Ticket(models.Model):
	ticket_name = models.CharField(max_length = 40)
	description = models.TextField()
	start_time = models.DateTimeField()
	end_time = models.DateTimeField()
	project = models.ForeignKey(Project, related_name="tickets")
	status = models.ForeignKey(Status, related_name="tickets")
	user = models.ForeignKey(User, related_name="tickets")

	def __unicode__(self):
		return self.ticket_name
	

class ProjectForm(ModelForm):

	class Meta:
		model = Project
		widgets = {'start_date' : SelectDateWidget(), 'end_date' : SelectDateWidget()}

class TicketForm(ModelForm):

	class Meta:
		model = Ticket
		exclude = ('project', 'user')
		widgets = {'start_time' : SelectDateWidget(), 'end_time' : SelectDateWidget()}

class LoginForm(forms.Form):
	username = forms.CharField(max_length = 20)
	password = forms.CharField(max_length = 20, widget=forms.PasswordInput)

	










