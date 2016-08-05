#!/usr/bin/env python3

import os, sys
# six is used for py2/py3 compatability
# PY3 is true if you are in Python3, else false. Used to guide the zip error import below.
# BytesIO gives us a file-like obect that can be opened by imread()
from six import PY3, BytesIO
# map/filter/reduce are lazily evaluated and run-once as in py3.
# Also, since reduce moved between py2 and py3, this imports is correctly in either.
from six.moves import map, filter, reduce
import zipfile
if PY3:
    from zipfile import BadZipFile
else:
    from zipfile import error as BadZipFile

from scipy.ndimage import imread
from skimage import color
from skimage.transform import resize

import re
import numpy as np

from catfinder.loaders import util

# I am putting this function right into a module and not declaring a class,
# because the class would be a singleton and singleton classes are a little silly
# in Python. I am not averse to changing this though.

train_zip_path = '../data/train.zip'
if not os.path.isfile(train_zip_path):
    raise Exception("Can't find train.zip")

jpg_re = re.compile(r'.*\.jp[e]?g$', re.IGNORECASE)

# Beware, this is specific to this zip file! As such, anything that won't generalize
# is hardcoded.
# Things that should generalize will be in util.py

cat_re = re.compile(r'.*cat.*', re.IGNORECASE)


def load_numpy(max_pos=-1, max_neg=-1, *, unpack = False, scale_to_largest_image=False, scale_to_size=None):
    # If you specify the maximum number of positive examples but not the maximum
    # number of negative examples, it tries to return a 50/50 split. That may not
    # actually make sense
    if max_neg==-1 and max_pos>-1:
        max_neg = max_pos

    if unpack:
        raise Exception('Unpacking to local FS is not supported yet')

    if scale_to_size is not None and scale_to_largest_image:
        raise Exception('Specify scaling to the largest image OR a size to scale to.')

    # Debatable whether this is actually needed.
    if scale_to_size is None and scale_to_largest_image:
        with zipfile.ZipFile(train_zip_path) as z:
            filelist = filter(jpg_re.match, z.namelist())
            scale_to_size = util.find_largest_image_in_zip(z, filelist)

    if scale_to_size is None and not scale_to_largest_image:
        # silently changing to a hardcoded value, beware!
        scale_to_size = [768,1024]

    n_pos = 0
    n_neg = 0
    X = list()
    y = list()
    # Actually do the load
    with zipfile.ZipFile(train_zip_path) as z:
        filelist = filter(jpg_re.match, z.namelist())
        for f in filelist:
            if cat_re.match(f) and n_pos != max_pos:
                y.append(1)
                n_pos += 1
                X.append(
                    util.process_img_from_file(
                        BytesIO(z.read(f)),
                        resize_dims = scale_to_size
                    )
                )
            elif (not cat_re.match(f)) and n_neg != max_neg:
                y.append(0)
                n_neg += 1
                X.append(
                    util.process_img_from_file(
                        BytesIO(z.read(f)),
                        resize_dims = scale_to_size
                    )
                )
            if n_pos == max_pos and n_neg == max_neg:
                break

    return (np.vstack(X), np.array(y
    ))
