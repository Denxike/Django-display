from django.contrib import admin
from .models import Item # Import the Item model

# Register your models here.

admin.site.register(Item) # Register the Item model with the Django admin site
