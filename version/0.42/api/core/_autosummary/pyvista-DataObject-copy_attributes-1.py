import pyvista as pv
source = pv.ImageData(dimensions=(10, 10, 5))
source = source.compute_cell_sizes()
target = pv.ImageData(dimensions=(10, 10, 5))
target.copy_attributes(source)
target.plot(scalars='Volume', show_edges=True)
