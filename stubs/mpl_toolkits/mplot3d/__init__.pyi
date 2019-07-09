from typing import Sequence

class Axes3D:

    def plot(self, xs: Sequence, ys: Sequence, zs: Sequence, **kwargs): ...
    def scatter(self, xs: Sequence, ys: Sequence, zs: Sequence, **kwargs): ...
    def plot_surface(self, X: Sequence, Y: Sequence, Z: Sequence, *args, **kwargs): ...
