import pytest
from hypothesis import given, settings
import hypothesis.strategies as hs

from scipy.ndimage import generic_filter, generic_filter1d, geometric_transform
import numpy as np
from llc import jit_filter_function, jit_filter1d_function


def fnc_zero(values):
    return values[0]*0


def fnc_zero_inplace(iline, oline):
    oline[...] = iline[0]*0.0


@given(hs.lists(hs.integers(5, 15), min_size=1, max_size=3),
       hs.integers(1, 5)
)
@settings(deadline=10000)
def test_generic_filter(arr_dim, fsize):
    arr = np.random.random(arr_dim)
    footprint = [d//fsize for d in arr_dim]
    # just make sure it runs
    filtered = generic_filter(arr, jit_filter_function(fnc_zero), size=footprint)
    assert np.allclose(filtered, 0.0)


@given(hs.lists(hs.integers(5, 15), min_size=2, max_size=2),
       hs.integers(1, 5)
)
@settings(deadline=10000)
def test_generic_filter1d(arr_dim, fsize):
    arr = np.random.random(arr_dim)
    axis = np.random.randint(0, arr.ndim-1)
    fsize = arr_dim[axis]//fsize
    # just make sure it runs
    filtered = generic_filter1d(arr, jit_filter1d_function(fnc_zero_inplace), fsize, axis=axis)
    assert np.allclose(filtered, 0.0)

