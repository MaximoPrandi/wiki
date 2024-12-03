from django.shortcuts import render

from ..controllers import index_controller


def index_view(request):
    return render(request, "encyclopedia/index.html", index_controller())