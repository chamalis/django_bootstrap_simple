from django.forms import ModelForm
from persons.models import Person

class addPersonForm(ModelForm):
    class Meta:
        model = Person
        fields = '__all__' # ['creation_date']

class searchPersonForm(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
