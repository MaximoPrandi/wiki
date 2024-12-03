from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect
from django.shortcuts import render

from ..controllers import new_post_controller, new_get_controller


def new_view(request):
    if request.POST:
        
        if isinstance((search_result := new_post_controller(request)), HttpResponseRedirect|HttpResponsePermanentRedirect):
            return search_result
        
        return render(request, "encyclopedia/new.html", new_post_controller(request))
    else:
        return render(request, "encyclopedia/new.html", new_get_controller(request))