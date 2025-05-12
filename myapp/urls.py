from django.urls import path
from . import views # Import views from the current app

urlpatterns = [
    path('', views.item_list, name='item_list'), # Map the root URL of the app to the item_list view
]
