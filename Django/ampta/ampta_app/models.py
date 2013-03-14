from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import iri_to_uri
from django.forms import ModelForm
from django.forms.extras.widgets import SelectDateWidget
from django import forms
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple
from django.forms.fields import datetime
from django.contrib.admin import widgets

import datetime

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
	
	def owned_by_user(self, user):
		return self.user == user

	def owned_by_user2(self, user):
		return self.project.owner == user




class LoginForm(forms.Form):
	username = forms.CharField(max_length = 20)
	password = forms.CharField(max_length = 20, widget=forms.PasswordInput)




		


