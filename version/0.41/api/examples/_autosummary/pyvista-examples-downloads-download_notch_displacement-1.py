from pyvista import examples
dataset = examples.download_notch_displacement()
dataset.plot(cmap='bwr')
