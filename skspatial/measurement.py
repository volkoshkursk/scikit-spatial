"""Measurements using spatial objects."""

import numpy as np
from dpcontracts import ensure

from skspatial.objects import Vector


@ensure("The output must be zero or greater.", lambda _, result: result >= 0)
@ensure("The output must be a numpy scalar.", lambda _, result: isinstance(result, np.number))
def area_triangle(point_a, point_b, point_c):
    """
    Return the area of a triangle defined by three points.

    The points are the three vertices of the triangle.

    Parameters
    ----------
    point_a : array_like
        Input point A.
    point_b : array_like
        Input point B.
    point_c : array_like
        Input point C.

    Returns
    -------
    scalar
        The area of the triangle.

    Examples
    --------
    >>> from skspatial.measurement import area_triangle
    >>> from skspatial.objects import Point

    >>> area_triangle([0, 0], [0, 1], [1, 0])
    0.5

    >>> area_triangle([0, 0], [0, 2], [1, 1])
    1.0

    References
    ----------
    http://mathworld.wolfram.com/TriangleArea.html

    """
    vector_ab = Vector.from_points(point_a, point_b)
    vector_ac = Vector.from_points(point_a, point_c)

    vector_cross = vector_ab.cross(vector_ac)

    return 0.5 * vector_cross.magnitude


@ensure("The output must be zero or greater.", lambda _, result: result >= 0)
@ensure("The output must be a numpy scalar.", lambda _, result: isinstance(result, np.number))
def volume_tetrahedron(point_a, point_b, point_c, point_d):
    """
    Return the volume of a tetrahedron defined by four points.

    The points are the four vertices of the tetrahedron.

    Parameters
    ----------
    point_a : array_like
        Input point A.
    point_b : array_like
        Input point B.
    point_c : array_like
        Input point C.
    point_d : array_like
        Input point D.

    Returns
    -------
    scalar
        The volume of the tetrahedron.

    Examples
    --------
    >>> from skspatial.measurement import volume_tetrahedron
    >>> from skspatial.objects import Point

    >>> volume_tetrahedron([0, 0], [3, 2], [-3, 5], [1, 8])
    0.0

    >>> volume = volume_tetrahedron([0, 0], [2, 0], [1, 1], [0, 0, 1])
    >>> volume.round(3)
    0.333

    References
    ----------
    http://mathworld.wolfram.com/Tetrahedron.html

    """
    vector_ab = Vector.from_points(point_a, point_b)
    vector_ac = Vector.from_points(point_a, point_c)
    vector_ad = Vector.from_points(point_a, point_d)

    vector_cross = vector_ac.cross(vector_ad)

    return 1 / 6 * abs(vector_ab.dot(vector_cross))
