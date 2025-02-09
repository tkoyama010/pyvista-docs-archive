from pyvista import examples
dataset = examples.download_cow()
dataset.plot(cpos="xy")
#
# This dataset is used in the following examples:
#
# * :ref:`extract_edges_example`
# * :ref:`mesh_quality_example`
# * :ref:`rotate_example`
# * :ref:`linked_views_example`
