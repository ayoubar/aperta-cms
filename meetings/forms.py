# coding=utf-8

from datetime import date

from django.conf import settings
from django.forms import Form, ModelForm, TextInput, Textarea, HiddenInput, CharField, ModelChoiceField, BooleanField, DateField, ModelMultipleChoiceField, CheckboxSelectMultiple, FileField, IntegerField

from members.functions import get_active_members

from .models import Meeting

#meeting form
class MeetingForm(ModelForm):
  additional_message 	= CharField(label='Message supplémentaire',widget=Textarea(attrs={'placeholder': "Message à transmettre dans l'invitation.",}),required=False)
  send 			= BooleanField(label='Envoi direct des invitations',required=False)

  class Meta:
    model = Meeting
    fields = ( 'title', 'when', 'time', 'location', 'num', 'deadline', 'additional_message', 'send', )
    widgets = {
#      'title'	: TextInput(attrs={'readonly': 'readonly', }),
      'when'	: TextInput(attrs={'type': 'date', }),
#      'time'	: TextInput(attrs={'type': 'time', }),
      'deadline': TextInput(attrs={'type': 'datetime', }),
      'num'	: HiddenInput(),
    }


#modify wizard forms
class ListMeetingsForm(Form):
  meetings = ModelChoiceField(queryset=Meeting.objects.all().order_by('-num'))

class ModifyMeetingForm(ModelForm):
  attendance = BooleanField(label='Inscrire/excuser un membre')

  class Meta:
    model = Meeting
    fields = ( 'title', 'when', 'time', 'location', 'attendance', )
    widgets = {
      'when'	: TextInput(attrs={'type': 'date', }),
      'time'	: TextInput(attrs={'type': 'time', }),
    }


#report form
class MeetingReportForm(Form):
  num		= IntegerField(widget=HiddenInput())
  title		= CharField(label=u'Titre',widget=TextInput(attrs={'readonly': 'readonly', }))
  when		= CharField(label=u'Date',widget=TextInput(attrs={'readonly': 'readonly', }))
  report	= FileField(label='Compte rendu')
  send 		= BooleanField(label='Envoi du compte rendu aux membres',required=False)

