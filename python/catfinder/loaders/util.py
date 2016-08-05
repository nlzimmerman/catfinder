#!/usr/bin/env python3

from six.moves import reduce
from six import BytesIO
from scipy.ndimage import imread

from scipy.ndimage import imread
from skimage import color
from skimage.transform import resize

def find_largest_image_in_zip(z, filelist):
    # z is a zipfile.ZipFile object, filelist is an iterator that tells us what files in the zip to check
    return reduce(
        lambda x, y: [max(x[0], y[0]), max(x[1], y[1])],
        (imread(BytesIO(z.read(f))).shape[:2] for f in filelist)
        )

def process_img_from_file(f, resize_dims=None, color_images=False):
    # f is a file handle or a BytesIO, this returns an image that is processed appropriately.

    # raw color image as an [x,y,3] nparray
    img = imread(f)
    if resize_dims is not None:
        img = resize(img, resize_dims)

    # If color is false, use color.rgb2gray to turn it into an [x,y] nparray.
    if not color_images:
        img = color.rgb2gray(img)

    # More logic will probably go here at some point.

    return img.flatten()
