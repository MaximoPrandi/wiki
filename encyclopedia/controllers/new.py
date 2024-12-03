from django.shortcuts import redirect
from urllib.parse import quote_plus
from numpy.random import randint
from django.urls import reverse

from ..util import save_entry, list_entries
from ..forms import NewForm
from .default import render_data


def new_post_controller(request):
    render_data["random_entry"] = list_entries()[randint(1, len(list_entries()))]
    
    form_response = NewForm(request.POST)
    
    if form_response.is_valid():
        save_entry(form_response.cleaned_data["title"], form_response.cleaned_data["data"])
        
        return redirect(reverse("encyclopedia:entry", args=(quote_plus(form_response.cleaned_data["title"]),)))
    else: 
        render_data["NewForm"] = form_response
        
    return render_data

def new_get_controller(request) -> dict:
    render_data["random_entry"] = list_entries()[randint(1, len(list_entries()))]
    render_data["NewForm"] = NewForm()

    return render_data