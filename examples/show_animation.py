from blobmodel import Model

bm = Model(Nx=100, Ny=50, Lx=10, Ly=10, dt=0.1, T=20, blob_shape='gauss')

bm.sample_blobs(num_blobs=1000)

# show animation and save as gif
bm.show_model(interval=100, save = True, gif_name = 'example.gif', fps = 10)