Slugifier – utilities set for slugify
=================

Django helper for slugify model's FileField and ImageField filenames

### Usage:

```python
from slugifier.utils import upload_to_slugify

class ModelName(models.Model):
    field_name = models.FileField('field_name', upload_to=upload_to_slugify('upload_dir_name'))
```

### Compability:
* For Django > 1.6 and Python 3.x use latest version
* For Django > 1.6 and Python 2.x use > 0.0.1 <= 0.0.6
* For Django 1.6 use version 0.0.1
