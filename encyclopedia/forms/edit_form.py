from django.forms import Form, CharField, Textarea

class EditForm(Form):
    data = CharField(min_length=1, label="Entry content*", required=False, widget=Textarea())