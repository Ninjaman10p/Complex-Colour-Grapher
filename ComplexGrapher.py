"""Graph complex functions using domain colouring."""


import numpy as np
from PIL import Image, ImageDraw
import itertools
import colorsys
from IPython.display import display
import warnings


def _rect(*args):
    if len(args) == 1:
        size = args[0]
    elif len(args) == 2:
        size = args
    else:
        raise TypeError("rect was expecting either 1 tuple or two ints")
    return itertools.product(range(size[0]), range(size[1]))


def _mapz(i, j, pos, size):
    z0 = pos[0]
    stretch = pos[1] - pos[0]
    z = z0 + np.real(stretch)*i/size[0] + 1j*np.imag(stretch)*j/size[1]
    return z


def _zmap(z, pos, size):
    z0 = pos[0]
    stretch = pos[1]-pos[0]
    x = (np.real(z) - np.real(z0))*size[0]/np.real(stretch)
    y = (np.imag(z) - np.imag(z0))*size[1]/np.imag(stretch)
    return (x, y)


def graph(f=(lambda z: z),
          pos=(-10+10j, 10-10j),
          size=(500, 500), dist=0.2,
          axis=False,
          grid=False,
          displayOnCompletion=True):
    """Complete the complex graph."""
    img = Image.new('RGB', size)
    pix = img.load()
    draw = ImageDraw.Draw(img)
    origin = _zmap(0, pos, size)
    warnings.filterwarnings('ignore')
    for i, j in _rect(size):
        try:
            z = _mapz(i, j, pos, size)
            out = f(z)
            bri = np.absolute(out) / dist
            bri = max(0, min(1, bri))
            hue = np.angle(out, deg=True)
            hue /= 360
            if hue < 0:
                hue += 1
            col = colorsys.hsv_to_rgb(hue, 1, bri)
            col = tuple(int(i*255) for i in col)
        except (ZeroDivisionError, ValueError):
            col = (255,)*3
        if grid:
            exp1 = (np.real(z) ==
                    int(np.real(z)) and np.imag(z) == int(np.imag(z)))
            exp2 = (abs(i - origin[0]) == 1) and j == origin[1]
            exp3 = (abs(j - origin[1]) == 1) and i == origin[0]
            if exp1 or exp2 or exp3:
                col = (255, 255, 255)
        pix[i, j] = col
    warnings.filterwarnings('default')
    if axis:
        draw.line((origin[0], 0, origin[0], size[0]))
        draw.line((0, origin[1], size[1], origin[1]))
    if displayOnCompletion:
        display(img)
    return img


# visual functions
def spiral(z):
    """Generate a spiral pattern."""
    return z*1j**np.absolute(z)


def invn(z, pos=0, rot=True):
    """Generate the inverse of a node.

    Use anticlockwise/clockwise instead
    """
    temp = 1/(z-pos)
    if not rot:
        temp = np.conj(temp)
    return temp


def cnorm(z):
    """Normalise a complex number."""
    return z/abs(z)
