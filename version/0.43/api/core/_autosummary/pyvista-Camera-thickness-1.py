import pyvista as pv
pl = pv.Plotter()
pl.camera.thickness
# Expected:
## 1000.0
pl.camera.thickness = 100
pl.camera.thickness
# Expected:
## 100.0
