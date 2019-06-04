from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class folder_file(MPTTModel):
    get_family
    name = models.CharField(max_length=120)
    parent = TreeForeignKey('self', on_delete=models.CASCADE,
                            null=True, blank=True, related_name='children')

    def __str__(self):
        return self.name
