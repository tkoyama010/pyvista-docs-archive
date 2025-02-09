# Create a DataSet with a variety of arrays.
#
import pyvista as pv
mesh = pv.Cube()
mesh.clear_data()
mesh.point_data['point-data'] = range(mesh.n_points)
mesh.cell_data['cell-data'] = range(mesh.n_cells)
mesh.field_data['field-data'] = ['a', 'b', 'c']
mesh.array_names
# Expected:
## ['point-data', 'field-data', 'cell-data']
#
# Get the point data array.
#
mesh.get_array('point-data')
# Expected:
## pyvista_ndarray([0, 1, 2, 3, 4, 5, 6, 7])
#
# Get the cell data array.
#
mesh.get_array('cell-data')
# Expected:
## pyvista_ndarray([0, 1, 2, 3, 4, 5])
#
# Get the field data array.
#
mesh.get_array('field-data')
# Expected:
## pyvista_ndarray(['a', 'b', 'c'], dtype='<U1')
