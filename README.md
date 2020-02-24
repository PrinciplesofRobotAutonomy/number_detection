# 3-Digit Number Detection

Using neural networks to build an automatic number plate recognition system.
See [this blog post](http://matthewearl.github.io/2016/05/06/cnn-anpr/) for an
explanation. This repo is based on [Deep ANPR repo](https://github.com/matthewearl/deep-anpr/).

Usage is as follows:

1. `./extractbgs.py SUN397.tar.gz`: Extract ~3GB of background images from the [SUN database](http://groups.csail.mit.edu/vision/SUN/)
   into `bgs/`. (`bgs/` must not already exist.) The tar file (36GB) can be [downloaded here](http://vision.princeton.edu/projects/2010/SUN/SUN397.tar.gz).
   This step may take a while as it will extract 108,634 images.

2. `./gen.py 1000`: Generate 1000 test set images in `test/`. (`test/` must not
    already exist.) This step requires `palab.ttf`, which is bold Palatino Linotype, to be in the
    `fonts/` directory. You can include other font weights/types in `fonts/` directory to improve generalizability. But we will use only bold Palatino Linotype for the class project.

3. `./train.py`: Train the model. A GPU is recommended for this step. It will
   take around a few hours to converge, depending on your network structure, fonts, etc. When you're satisfied that the
   network has learned enough press `Ctrl+C` and the process will write the
   weights to `weights.npz` and return.

4. `./detect.py in.jpg weights.npz out.jpg`: Detect number plates in an image.

The project has the following dependencies:

* [TensorFlow](https://tensorflow.org)
* OpenCV
* NumPy
