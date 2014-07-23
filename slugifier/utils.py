import os
from django.utils.text import slugify

def upload_to_slugify(upload_path):
    """
    This method save ImageField class file in 'upload_to_path' with slugify it's name.
    """
    def upload_to_slugify_inner(instance, filename):
        name, ext = os.path.splitext(filename)
        f = slugify(name) + ext
        return os.path.join(upload_path, f)
    return upload_to_slugify_inner
