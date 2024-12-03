from urllib.parse import unquote
from numpy.random import randint
from markdown2 import Markdown

from ..util import get_entry, list_entries
from .default import render_data


def entry_controller(entry) -> dict:
    render_data["random_entry"] = list_entries()[randint(1, len(list_entries()))]
    
    entry = unquote(entry)
    
    if (data := get_entry(entry)):
        data = Markdown().convert(data)
        default = None
    else:
        default = f"<h1>Error 404.</h1><br><h3>Entry '{entry}' not found</h3>"
    
    render_data.update({
        "data": data,
        "entry": entry,
        "default": default,
    })
    
    return render_data