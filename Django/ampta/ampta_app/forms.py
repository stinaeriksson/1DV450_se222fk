# -*- coding: utf-8 -*-
from django import forms
from django.contrib.admin import widgets   
from django.db import models                                    
from django.forms import ModelForm
from ampta_app.models import Ticket, Project
from django.forms.extras.widgets import SelectDateWidget
from django.utils.encoding import iri_to_uri

class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        exclude = ('project', 'user', )


    def __init__(self, *args, **kwargs):
        super(TicketForm, self).__init__(*args, **kwargs)
      
        self.fields['start_time'].widget = widgets.AdminSplitDateTime()
        self.fields['end_time'].widget = widgets.AdminSplitDateTime()

        self.fields['ticket_name'].label = "Namn på ticket"
        self.fields['description'].label = "Beskrivning"
        self.fields['start_time'].label = "Startar"
        self.fields['end_time'].label = "Slutar"
        self.fields['description'].widget.attrs['rows'] = 4
       
       
class ProjectForm(ModelForm):

    class Meta:
        model = Project
        exclude = ('owner')
    
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
      
        self.fields['start_date'].widget = widgets.AdminDateWidget()
        self.fields['end_date'].widget = widgets.AdminDateWidget()

        self.fields['project_name'].label = "Projektets namn"
        self.fields['description'].label = "Beskrivning"
        self.fields['start_date'].label = "Startar"
        self.fields['end_date'].label = "Slutar"
        self.fields['users'].label = "Medlemmar i projektet"
        self.fields['description'].widget.attrs['rows'] = 4


class LoginForm(forms.Form):
    username = forms.CharField(max_length = 20)
    password = forms.CharField(max_length = 20, widget=forms.PasswordInput)

