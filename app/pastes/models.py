import uuid
from django.db import models

hash_width = 8

class pastebin_entry(models.Model):
    """
    This class generates a UUID and stores a text field

    TODO I may want to switch this over to having two classes, one for holding the unique ID
    and the other for holding the paste itself.
    """
    
    date_of_post = models.DateTimeField("creation date")
    id = models.UUIDField( primary_key=True, default = uuid.uuid4, editable = False )
    pastebin_entry_title = models.CharField(max_length = 100)
    pastebin_entry_string = models.TextField()

    
    def __str__(self):
        return str(id)[0:hash_width]
