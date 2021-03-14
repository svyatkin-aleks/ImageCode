from django.db import models

import struct
from PIL import Image


def get_image_color(filename):
    image = Image.open(filename)
    image_rgb = image.convert('RGB')
    rgb = image_rgb.getcolors(maxcolors=256000)[0][1]
    return '#%02x%02x%02x' % rgb


class ImageCode(models.Model):
    image = models.ImageField()
    code = models.CharField(max_length=100, blank=True)

    def save(self, *args, **kwargs):
        self.code = get_image_color(self.image)
        super(ImageCode, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.image.name} - {self.code}'
# Create your models here.
