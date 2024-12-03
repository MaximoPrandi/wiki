from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect
from django.shortcuts import render

from ..controllers import edit_post_controller, edit_get_controller


def edit_view(request, entry):
    if request.POST:
        
        if isinstance((search_result := edit_post_controller(request, entry)), HttpResponseRedirect|HttpResponsePermanentRedirect):
            return search_result
        
        return render(request, "encyclopedia/edit.html", search_result)
    else:
        return render(request, "encyclopedia/edit.html", edit_get_controller(entry))