# Find the index of the closest point to ``(0, 1, 0)``.
#
import pyvista as pv
mesh = pv.Sphere()
index = mesh.find_closest_point((0, 1, 0))
index
# Expected:
## 239
#
# Get the coordinate of that point.
#
mesh.points[index]
# Expected:
## pyvista_ndarray([-0.05218758,  0.49653167,  0.02706946], dtype=float32)
