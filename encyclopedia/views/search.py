from django.http import (HttpResponsePermanentRedirect, HttpResponseRedirect)
from django.shortcuts import render

from ..controllers import search_controller


def search_view(request):
    if request.method == "POST":
        
        if isinstance((search_result := search_controller(request)), HttpResponseRedirect|HttpResponsePermanentRedirect):
            return search_result
        
        return render(request, "encyclopedia/search.html", search_result)