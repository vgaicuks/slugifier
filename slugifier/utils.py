import os
from django.utils.text import slugify
from django.utils.deconstruct import deconstructible

@deconstructible
class UploadToSlugify(object):

    def __init__(self, path):
        self.path = path

    def __call__(self, instance, filename):
        name, ext = os.path.splitext(filename)
        f = slugify(name) + ext
        return os.path.join(self.path, f)

# Backward compatibility
def upload_to_slugify(path="/"):
    return UploadToSlugify(path)
