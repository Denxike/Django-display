from django.shortcuts import render
from .models import Item # Import the Item model

# Create your views here.

def item_list(request):
    """
    View to display a list of all items.
    """
    items = Item.objects.all() # Get all Item objects from the database
    context = {
        'items': items # Pass the list of items to the template context
    }
    return render(request, 'myapp/item_list.html', context) # Render the item_list.html template
