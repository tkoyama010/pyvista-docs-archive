# Create a mesh, add scalars to the mesh, and return the active
# scalars info.  Note how when the scalars are added, they
# automatically become the active scalars.
#
import pyvista as pv
mesh = pv.Sphere()
mesh['Z Height'] = mesh.points[:, 2]
mesh.active_scalars_info
# Expected:
## ActiveArrayInfoTuple(association=<FieldAssociation.POINT: 0>, name='Z Height')
