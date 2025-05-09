from django import forms
from .models import ChatMessage, CalendarEvent

class ChatMessagesForm(forms.ModelForm):
    class Meta:
        model = ChatMessage
        fields = '__all__'

class CalendarEventForm(forms.ModelForm):
    class Meta:
        model = CalendarEvent
        fields = '__all__'
