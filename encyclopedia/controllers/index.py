from ..util import list_entries
from .default import render_data

from numpy.random import randint


def index_controller():
    render_data["entries"] = list_entries()
    render_data["random_entry"] = list_entries()[randint(1, len(list_entries()))]
    
    return render_data