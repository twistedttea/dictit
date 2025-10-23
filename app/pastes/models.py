import string, random
from django.db import models

url_width = 8


def generate_short(length):
    """
    generates urls to find pastes by
    """
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(length))


class pastebin_entry(models.Model):
    """
    creates short_id
    saves date of creation
    saves title
    saves post contents
    """

    short_id = models.CharField(max_length=10, unique=True, editable=False)
    date = models.DateTimeField("creation date", auto_now_add=True)
    title = models.CharField(max_length=100)
    private = models.BooleanField(default=True)
    content = models.TextField()

    def save(self, *args, **kwargs):
        if not self.short_id:
            new_id = generate_short(url_width)
            while pastebin_entry.objects.filter(short_id=new_id).exists():
                new_id = generate_short(url_width)
            self.short_id = new_id
        super().save(*args, **kwargs)

    def __str__(self):
        return self.short_id
