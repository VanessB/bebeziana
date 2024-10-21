default_seed = 42


def seed_basic(seed=default_seed):
    import os
    import random

    random.seed(seed)
    os.environ['PYTHONHASHSEED'] = str(seed)


def seed_numpy(seed=default_seed):
    import numpy

    numpy.random.seed(seed)


# tensorflow random seed 
def seed_tensorflow(seed=default_seed):
    import tensorflow

    tensorflow.random.set_seed(seed)


# torch random seed
def seed_torch(seed=default_seed):
    import torch

    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False


def seed_everything(seed=default_seed,
                    to_be_seeded: list[str] = ["basic", "numpy", "tensorflow", "torch"]):
    for name in to_be_seeded:
        try:
            globals()["seed_" + name](seed)
        except Exception as exception:
            print(exception)
