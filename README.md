# Complex Colour Grapher
 
<p>A python script that can create colour-based graphs of complex functions. The hue is equivalent to the direction from the origin (e.g. red=positive, cyan=negative), and the brightness is lowered close to zero (any zeroes are displayed as black)</p>

<p>Based on domain colouring method of displaying complex numbers<br>
 <i>Written in an iPython notebook, you can use JupyterNotebook to view</i></p>

### Functions
> graph(f=(lambda z:z), pos=(-10+10j, 10-10j), size=(500,500), dist=0.2, axis=False, grid=False)
>><b>Main graphing function</b><br>
>> f: takes in a single argument function (or other callable object). This function must be able to handle complex numbers, and output a complex number. This is the function that is graphed<br>
>> pos: a 2-tuple of complex numbers. The first tuple is the number displayed in the top left corner, the second in the bottom right<br>
>> size: the resolution of the rendered image (2-tuple)<br>
>> dist: A multiplier for the black regions (zeroes). Larger number -> larger darkened region<br>
>> axis: display an axis on the rendered image (centred on the origin)<br>
>> grid: display a grid of dots at each complex-integer on the image (0+0j, 0+1j, 1+0j, 1+1j...)<br>

> \_mapz(i,j,pos,size)
>><b>An internal function, maps the point (i,j) to the equivalent complex number in size, where the cornets are pos</b>

> \_zmap(z,pos,size)
>> <b>An internal function, the inverse of _mapz()</b>

> \_rect(\*args)
>><b>An internal function. Takes in either a 2-tuple of ints or two ints and returns the product of their ranges</b>
