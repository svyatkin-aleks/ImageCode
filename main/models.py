from django.db import models

import struct
from PIL import Image
import scipy
import scipy.misc
import scipy.cluster

NUM_CLUSTERS = 5


def _get_dominant_color(image_file):
    """
    Take a file object and return the colour in hex code
    """

    im = image_file
    im = im.resize((150, 150))  # optional, to reduce time
    ar = scipy.misc.fromimage(im)
    shape = ar.shape
    ar = ar.reshape(scipy.product(shape[:2]), shape[2])

    # print 'finding clusters'
    codes, dist = scipy.cluster.vq.kmeans(ar, NUM_CLUSTERS)
    # print 'cluster centres:\n', codes

    vecs, dist = scipy.cluster.vq.vq(ar, codes)  # assign codes
    counts, bins = scipy.histogram(vecs, len(codes))  # count occurrences

    index_max = scipy.argmax(counts)  # find most frequent
    peak = codes[index_max]
    colour = ''.join(chr(c) for c in peak).encode('hex')
    return colour


class ArticleImage(models.Model):

    def get_dominant_color(self):
        return _get_dominant_color(self.image.open())

    def set_article_color(self):
        self.article = self.get_dominant_color()

    article = models.CharField(max_length=100, blank=True)
    image = models.ImageField()



def get_colors(image_file, numcolors=10, resize=150):
    # Resize image to speed up processing
    img = Image.open(image_file)
    img = img.copy()
    img.thumbnail((resize, resize))

    # Reduce to palette
    paletted = img.convert('P', palette=Image.ADAPTIVE, colors=numcolors)

    # Find dominant colors
    palette = paletted.getpalette()
    color_counts = sorted(paletted.getcolors(), reverse=True)
    colors = list()
    for i in range(numcolors):
        palette_index = color_counts[i][1]
        dominant_color = palette[palette_index*3:palette_index*3+3]
        colors.append(tuple(dominant_color))

    return colors



# class Image(models.Model):
#     image = models.ImageField()
#
#     def get_dominant_color(self):
#         return _get_dominant_color(self.image.open())
#
#     def set_article_background_color(self):
#         self.code = self.get_dominant_color()
#
#     code = models.CharField(max_length=100, blank=True)


# Create your models here.
