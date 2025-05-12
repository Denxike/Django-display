from django.db import models

# Create your models here.

class Item(models.Model):
    """
    A simple model to represent an item with a name and description.
    """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True) # Description is optional
    created_at = models.DateTimeField(auto_now_add=True) # Automatically set on creation

    def __str__(self):
        """
        String representation of the Item model.
        """
        return self.name

