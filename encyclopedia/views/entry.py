from django.shortcuts import render

from ..controllers import entry_controller


def entry_view(request, entry):
    return render(request, "encyclopedia/entry.html", entry_controller(entry))