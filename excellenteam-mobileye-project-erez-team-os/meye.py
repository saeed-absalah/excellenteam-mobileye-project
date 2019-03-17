import numpy as np


class MEImage(object):
    def __init__(self, im, origin, rect):
        self.im = im
        self.origin = origin
        self.rect = rect

    @classmethod
    def from_file(cls, file_name, as_type=None):
        with open(file_name, 'r') as f:
            shape = np.fromfile(f, count=2, sep=' ').astype('int')
            origin = np.fromfile(f, count=2, sep=' ').astype('int')
            rect = np.fromfile(f, count=4, sep=' ').astype('int')
            im = np.fromfile(f, sep=' ').reshape(shape).astype('int')
        return cls(im, origin, rect)

    def to_file(self, file_name):
        with open(file_name, 'w') as f:
            np.array(self.im.shape).tofile(f, sep=' ')
            f.write(' ')
            self.origin.tofile(f, sep=' ')
            f.write(' ')
            self.rect.tofile(f, sep=' ')
            f.write(' ')
            self.im.tofile(f, sep=' ')
