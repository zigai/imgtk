# imgtk
[![PyPI version](https://badge.fury.io/py/imgtk-python.svg)](https://badge.fury.io/py/imgtk-python)
![Supported versions](https://img.shields.io/badge/python-3.10+-blue.svg)
[![Downloads](https://static.pepy.tech/badge/imgtk-python)](https://pepy.tech/project/imgtk-python)
[![license](https://img.shields.io/github/license/zigai/imgtk.svg)](https://github.com/zigai/imgtk/blob/main/LICENSE)
# Installation
#### From PyPi
```
pip install imgtk-python
```
#### From source
```
pip install git+https://github.com/zigai/imgtk.git
```

# Usage
```
usage: imgtk [--help] [-v] [--mode] MODE [-t] T [actions] [items]

options:
  --help                 show this help message and exit
  --mode                 display kept/discarded items (default: 'kept')
  -t                     number of threads to use (default: 23)
  -v, -verbose           verbose mode (extra log messages and progress bars)

filters:
  -w, --width            Filter by image width
  -h, --height           Filter by image height
  -sz, --size            Filter by file size
  -ar, --aspect-ratio    Filter by aspect ratio
  -fn, --filename        Filter by filename using glob or regex pattern matching
  -txt, --text           Filter by text content using OCR using glob or regex pattern matching

modifiers:
  -rs, --resize          Resize the image to the given size
  -cr, --crop            Crop the image to the given box
  -rot, --rotate         Rotate the image by the given angle
  -sc, --scale           Scale the image by the given factor
  -f, --filter           Apply the given filter to the image. Filters: [blur, contour, detail, edge_enhance, edge_enhance_more, emboss, find_edges, sharpen, smooth, smooth_more]
  -fl, --flip            Flip filter to flip an image horizontally or vertically
  -cnv, --convert        Convert the image to the given mode. Modes: [L, RGB, CMYK, GRAYSACLE]
  -inv, --invert         Invert filter to invert the colors of an image
  -thr, --threshold      Threshold filter to binarize an image
  -cont, --contrast      Adjust the image contrast
  -brgh, --brightness    Adjust the image brightness
  -shrp, --sharpness     Adjust the sharpness of the image
  -sat, --saturation     Adjust the image saturation
  -mb, --median-blur     Median blur filter to reduce noise in an image
  -gb, --gaussian-blur   Gaussian blur filter to reduce noise in an image
  -m, --move             Move the image to the given directory
  -s, --save             Save the image to the given directory

notes:
  filters can be inverted by adding a '!' after the flag
  you can get help for a specific action by running 'imgtk <action> --help'
```

# License
[MIT License](https://github.com/zigai/imgtk/blob/master/LICENSE)
