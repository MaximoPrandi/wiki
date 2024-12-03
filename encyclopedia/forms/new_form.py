from django.forms import Form, CharField, TextInput, Textarea
from django.core.validators import RegexValidator

from ..util import list_entries

validate_entry_title = RegexValidator( rf"^(?!.*\b({"|".join(list_entries())})\b).*$" )

class NewForm(Form):
    title = CharField(validators=[validate_entry_title], min_length=1, max_length=200, label="Entry title", widget=TextInput(attrs={"pattern":rf"^(?!.*\b({"|".join(list_entries())})\b).*$"}))
    data = CharField(min_length=1, label="Entry content*", required=False, widget=Textarea())