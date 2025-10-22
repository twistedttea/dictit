from django import forms
from django import forms

from .models import pastebin_entry


class paste_form(forms.ModelForm):
    class Meta:
        model = pastebin_entry
        fields = ["title", "content"]
        contentwidget = {"content": forms.Textarea(attrs={"rows": 25, "cols": 80})}

    # def sparkly_clean(self):
    #     content = self.cleaned_data["content"]
    #     return bleach.clean(content, strip=True)
