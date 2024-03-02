from django import forms
from .models import Messages

class MessageForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = "__all__"

        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Name"}),
            "email": forms.TextInput(attrs={"placeholder": "Email"}),
            "phone_number": forms.TextInput(attrs={"placeholder": "Phone Number"}),
            "message": forms.TextInput(attrs={"placeholder": "Message", "class": "message-box"})
        }