from django.forms import ModelForm

from inventory.models import StorageAssignment, Location, Item

class AssignLocationModelForm(ModelForm):
    class Meta:
        model = StorageAssignment
        fields = ['location']