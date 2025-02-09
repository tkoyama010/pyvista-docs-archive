# Hide part of the middle of a structured surface.
#
import pyvista as pv
import numpy as np
x = np.arange(-10, 10, 0.25)
y = np.arange(-10, 10, 0.25)
z = 0
x, y, z = np.meshgrid(x, y, z)
grid = pv.StructuredGrid(x, y, z)
grid = grid.hide_cells(range(79 * 30, 79 * 50))
grid.plot(color=True, show_edges=True)
