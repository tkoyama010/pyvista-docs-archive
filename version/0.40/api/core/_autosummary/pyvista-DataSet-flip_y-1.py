import pyvista
from pyvista import examples
pl = pyvista.Plotter(shape=(1, 2))
pl.subplot(0, 0)
pl.show_axes()
mesh1 = examples.download_teapot()
_ = pl.add_mesh(mesh1)
pl.subplot(0, 1)
pl.show_axes()
mesh2 = mesh1.flip_y(inplace=False)
_ = pl.add_mesh(mesh2)
pl.show(cpos="xy")
