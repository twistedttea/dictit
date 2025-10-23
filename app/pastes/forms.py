from django import forms

from .models import pastebin_entry


class paste_form(forms.ModelForm):
    class Meta:
        model = pastebin_entry
        fields = ["title", "content", "private"]


class search_paste_form(forms.Form):
    title = forms.CharField(required=False, label="Title")
    short_id = forms.CharField(required=False, label="Short ID")
