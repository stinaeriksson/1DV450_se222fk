from django import template

register = template.Library()

@register.filter(name='ownership')
def ownership(project, user):
	return project.owner == user

@register.filter(name='ticket_ownership')
def ticket_ownership(ticket, user):
	return ticket.user == user

@register.filter(name='ticket_project_ownership')
def ticket_project_ownership(ticket, user):
	return ticket.project.owner == user