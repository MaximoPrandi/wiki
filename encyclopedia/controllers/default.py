from numpy.random import randint

from ..forms import SearchForm
from ..util import list_entries


render_data = { 
    "SearchForm": SearchForm(),
    "random_entry": list_entries()[randint(1, len(list_entries()))]
}