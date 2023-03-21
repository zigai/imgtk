# imgtk
[![PyPI version](https://badge.fury.io/py/imgtk-py.svg)](https://badge.fury.io/py/imgtk-py)
![Supported versions](https://img.shields.io/badge/python-3.10+-blue.svg)
[![Downloads](https://static.pepy.tech/badge/imgtk-py)](https://pepy.tech/project/imgtk-py)
[![license](https://img.shields.io/github/license/zigai/imgtk.svg)](https://github.com/zigai/imgtk/blob/main/LICENSE)
# Installation
#### From PyPi
```
pip install imgtk-py
```
#### From source
```
pip install git+https://github.com/zigai/imgtk.git
```

# Usage
```
Filters can be inverted by adding a '!' after the flag .

options:
  -help                show this help message and exit
  -t                   number of threads to use (default: 7)
  -v, -verbose         verbose mode (extra log messages and progress bars)

filters:
  -w, -width           Filter by image width
  -h, -height          Filter by image height
  -ar, -aspect-ratio   Filter by aspect ratio
  -sz, -size           Filter by file size
  -fn, -filename       Filter by filename using glob or regex pattern matching
  -txt, -text          Filter by text content using OCR using glob or regex pattern matching

transformers:
  -sc, -scale          Scale the image by the given factor
  -f, -filter          Apply the given filter to the image. Filters: [blur, contour, detail, edge_enhance, edge_enhance_more, emboss, find_edges, sharpen, smooth, smooth_more]
  -mv, -move           Move the image to the given directory
  -s, -save            Save the image to the given directory
  -rs, -resize         Resize the image to the given size.
  -cnv, -convert       Convert the image to the given mode. Modes: [L, RGB, CMYK, GRAYSACLE]
  -cr, -crop           Crop the image to the given box.
```

# License
[MIT License](https://github.com/zigai/imgtk/blob/master/LICENSE)
