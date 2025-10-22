from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from .forms import paste_form
from .models import pastebin_entry


def create_paste(request):
    if request.method == "POST":
        form = paste_form(request.POST)
        if form.is_valid():
            paste = form.save()
            # send to user id field
            return redirect("view_paste", short_id=paste.short_id)
    else:
        form = paste_form()
    return render(request, "create_paste.html", {"form": form})


def view_paste(request, short_id):
    paste = get_object_or_404(pastebin_entry, short_id=short_id)
    return render(request, "view_paste.html", {"paste": paste})
