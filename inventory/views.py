from django.shortcuts import render
from django.views import generic
from pkg_resources import ResolutionError
from inventory.models import Item, Location, StorageAssignment
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from inventory.forms import AssignLocationModelForm

# Create your views here.

class ItemListView(generic.ListView):
    model = Item

class ItemDetailView(generic.DetailView):
    model = Item

class LocationListView(generic.ListView):
    model = Location

class LocationDetailView(generic.DetailView):
    model = Location

class ItemCreate(CreateView):
    model = Item
    fields = ['name', 'type', 'description']

class ItemUpdate(UpdateView):
    model = Item
    fields = ['name', 'type', 'description']

class ItemDelete(DeleteView):
    model = Item
    success_url = reverse_lazy('items')

class LocationCreate(CreateView):
    model = Location
    fields = ['address', 'city']

class LocationUpdate(UpdateView):
    model = Location
    fields = ['address', 'city']

class LocationDelete(DeleteView):
    model = Location
    success_url = reverse_lazy('locations')

def assign_item(request, pk):
    """View to Assign an inventory Item to a Location"""
    qitem = get_object_or_404(Item, id = pk)

    if request.method == 'POST':
        form = AssignLocationModelForm(request.POST)

        if form.is_valid():
            item_query = StorageAssignment.objects.filter(item = qitem)
            assigned_to = form.cleaned_data['location']
            
            if len(item_query) == 0:
                result=StorageAssignment(item=qitem, location = assigned_to) 
                result.save()   
            else:
                result = item_query[0]
                result.location = assigned_to 
                result.save()
                       
            return HttpResponseRedirect(reverse('item-detail', args=[str(qitem.id)]))
    else:
        form = AssignLocationModelForm()

    context = {
        'form': form,
        'item': qitem,
    } 

    return render(request, "inventory/item_assign.html", context) 

def index(request):
    """View for the home page"""

    num_items = Item.objects.all().count()
    num_locations = Location.objects.all().count()

    context = {
        'num_items': num_items,
        'num_locations': num_locations,
    }

    return render(request, 'index.html', context)

def page_not_found(request, exception):
    """Error view for a page not found"""
    return render(request, 'page_not_found.html')

def forbidden_request(request, exception):
    """Error view for a page not found"""
    return render(request, 'forbidden_request.html')