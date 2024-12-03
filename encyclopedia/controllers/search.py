from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect
from django.shortcuts import redirect
from urllib.parse import quote_plus
from numpy.random import randint
from django.urls import reverse

from ..util import get_entry, list_entries
from ..forms.search_form import SearchForm
from .default import render_data


def search_controller(request) -> dict|HttpResponseRedirect|HttpResponsePermanentRedirect:
    search_raw = SearchForm(request.POST)
    render_data["random_entry"] = list_entries()[randint(1, len(list_entries()))]
    
    if search_raw.is_valid():
        if get_entry(search := str(search_raw.cleaned_data["search"]).lower().capitalize()):
            return redirect(reverse("encyclopedia:entry", args=(quote_plus(search))))
        else:
            if not (coincidences := [entry for entry in list_entries() if search.lower() in entry.lower()]):
                render_data["default"] = f"No coincidence found for '{search_raw.cleaned_data["search"]}' "
            else:
                render_data["coincidences"] = coincidences
        render_data["search"] = search
        render_data["search_raw"] = search_raw.cleaned_data["search"]
    else:
        return redirect(reverse("encyclopedia:index"))
    
    return render_data