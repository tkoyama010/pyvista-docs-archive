import pyvista
sphere = pyvista.Sphere()
sphere.face_normals  # doctest:+SKIP
# Expected:
## pyvista_ndarray([[-0.05413816,  0.00569015, -0.9985172 ],
##                  [-0.05177207,  0.01682176, -0.9985172 ],
##                  [-0.04714328,  0.02721819, -0.9985172 ],
##                  ...,
##                  [-0.26742265, -0.02810723,  0.96316934],
##                  [-0.1617585 , -0.01700151,  0.9866839 ],
##                  [-0.1617585 , -0.01700151,  0.9866839 ]], dtype=float32)
