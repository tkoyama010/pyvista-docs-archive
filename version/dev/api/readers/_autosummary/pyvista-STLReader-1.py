import pyvista as pv
from pyvista import examples
filename = examples.download_cad_model(load=False)
filename.split("/")[-1]  # omit the path
# Expected:
## '42400-IDGH.stl'
reader = pv.get_reader(filename)
mesh = reader.read()
mesh.plot()
