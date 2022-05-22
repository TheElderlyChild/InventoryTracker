from django.db import models
from django.urls import reverse
import uuid

# Create your models here.
class Item(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.name + " (" + str(self.id) + ")"

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this item."""
        return reverse('item-detail', args=[str(self.id)])

    def get_location(self):
        """Gets the location of this Item"""
        sa = StorageAssignment.objects.filter(item = self)
        if len(sa) == 1:
            return sa[0].location

    def get_location_url(self):
        """Gets the url of this item's location"""
        sa = self.get_location()
        if sa == None:
            return ""
        else:
            return sa.get_absolute_url()

class Location(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    address = models.CharField(max_length=400)
    city = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.address + " in " + self.city

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this location."""
        return reverse('location-detail', args=[str(self.id)])

    def get_items(self):
        """Gets the items at this location"""
        record_list=sa = StorageAssignment.objects.filter(location = self)
        result = []
        for record in record_list:
            result.append(record.item)
        return result


class StorageAssignment(models.Model):
    assigned_date = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey('Location', on_delete=models.CASCADE)
    item = models.OneToOneField('Item', on_delete=models.CASCADE)

    def __str__(self):
        """String for representing the Model object."""
        return str(self.item) + " assigned to " + str(self.location) + " at " + str(self.assigned_date)
    