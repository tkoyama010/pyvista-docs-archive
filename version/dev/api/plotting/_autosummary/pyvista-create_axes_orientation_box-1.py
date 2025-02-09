# Create and plot an orientation box
#
import pyvista as pv
actor = pv.create_axes_orientation_box(
    line_width=1,
    text_scale=0.53,
    edge_color='black',
    x_color='k',
    y_color=None,
    z_color=None,
    xlabel='X',
    ylabel='Y',
    zlabel='Z',
    color_box=False,
    labels_off=False,
    opacity=1.0,
)
pl = pv.Plotter()
_ = pl.add_actor(actor)
pl.show()
