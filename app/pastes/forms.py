from django import forms

from .models import pastebin_entry


class paste_form(forms.ModelForm):
    class Meta:
        model = pastebin_entry
        fields = ["title", "content"]
        widget = {
            "content": forms.Textarea(attrs={
                "class": "form-text-field",
                "placeholder": "Enter text here.",
                "rows": 25,
                "cols": 80
            }),
            # "title": forms.CharField(attrs={
            #     "class": "form-control",
            #     "placeholder": "Enter paste title"
            # }),

        }

    # def sparkly_clean(self):
    #     content = self.cleaned_data["content"]
    #     return bleach.clean(content, strip=True)
