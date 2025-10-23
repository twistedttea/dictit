from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from .forms import paste_form
from .forms import search_paste_form
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


def search_paste(request):
    form = search_paste_form(request.GET or None)

    # If short_id is given, redirect immediately
    if form.is_valid() and form.cleaned_data.get("short_id"):
        short_id = form.cleaned_data.get("short_id")
        paste = get_object_or_404(pastebin_entry, short_id=short_id, private=False)
        return redirect(f"/p/{paste.short_id}")

    # Otherwise search by title
    results = pastebin_entry.objects.filter(private=False)  # Only public pastes

    if form.is_valid():
        title = form.cleaned_data.get("title")
        if title and (len(title) > 1):
            results = results.filter(title__icontains=title)

    paginator = Paginator(results, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "search_paste.html",
        {"form": form, "pastes": page_obj},
    )
