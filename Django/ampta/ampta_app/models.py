from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
	project_name = models.CharField(max_length = 40)
	description = models.TextField()
	start_date = models.DateField()
	end_date = models.DateField()
	owner = models.ForeignKey(User, related_name="projects")
	users = models.ManyToManyField(User, related_name="projects_user")

	def __unicode__(self):
		return self.project_name

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
	

