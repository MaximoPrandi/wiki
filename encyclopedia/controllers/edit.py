from django.shortcuts import redirect
from urllib.parse import quote_plus
from numpy.random import randint
from django.urls import reverse

from ..util import save_entry, get_entry, list_entries
from ..forms import EditForm
from .default import render_data


def edit_post_controller(request, entry):
    form_response = EditForm(request.POST)
    render_data["entry"] = entry
    
    if form_response.is_valid():
        save_entry(entry, form_response.cleaned_data["data"])
        
        return redirect(reverse("encyclopedia:entry", args=(quote_plus(entry),)))
    else: 
        render_data["EditForm"] = form_response
        
    return render_data

def edit_get_controller(entry) -> dict:
    render_data["random_entry"] = list_entries()[randint(1, len(list_entries()))]
    
    render_data.update({ 
        "EditForm": EditForm({"data":get_entry(entry)}),
        "entry":entry
    })

    return render_data