import pyvista as pv
pl = pv.Plotter()
pl.renderer.lights  # doctest:+SKIP
# Expected:
## [<Light (Headlight) at ...>,
##  <Light (Camera Light) at 0x7f1dd8155760>,
##  <Light (Camera Light) at 0x7f1dd8155340>,
##  <Light (Camera Light) at 0x7f1dd8155460>,
##  <Light (Camera Light) at 0x7f1dd8155f40>]
