from django.forms import Form, CharField, TextInput

class SearchForm(Form):
    search = CharField(label="",widget=TextInput(attrs={"placeholder": "Search Encyclopedia", "class":"search"}))