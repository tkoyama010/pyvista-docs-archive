from pyvista import examples
dataset = examples.download_notch_stress()
dataset.plot(cmap='bwr')
