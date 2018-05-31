import numba
from numba import cfunc, carray
from numba.types import intc, CPointer, float64, intp, voidptr
from scipy import LowLevelCallable


def jit_filter_function(filter_function):
    """Decorator for use with scipy.ndimage.generic_filter."""
    jitted_function = numba.jit(filter_function, nopython=True)

    @cfunc(intc(CPointer(float64), intp, CPointer(float64), voidptr))
    def wrapped(values_ptr, len_values, result, data):
        values = carray(values_ptr, (len_values,), dtype=float64)
        result[0] = jitted_function(values)
        return 1
    return LowLevelCallable(wrapped.ctypes)


def jit_filter1d_function(filter_function):
    """Decorator for use with scipy.ndimage.generic_filter1d."""
    jitted_function = numba.jit(filter_function, nopython=True)

    @cfunc(intc(CPointer(float64), intp, CPointer(float64), intp, voidptr))
    def wrapped(in_values_ptr, len_in, out_values_ptr, len_out, data):
        in_values = carray(in_values_ptr, (len_in,), dtype=float64)
        out_values = carray(out_values_ptr, (len_out,), dtype=float64)
        jitted_function(in_values, out_values)
        return 1
    return LowLevelCallable(wrapped.ctypes)


def jit_geometric_function(geometric_function):
    jitted_function = numba.jit(geometric_function, nopython=True)

    @cfunc(intc(CPointer(intp), CPointer(float64), intc, intc, voidptr))
    def wrapped(output_ptr, input_ptr, output_rank, input_rank, user_data):
        output_coords = carray(output_ptr, (output_rank,), dtype=intp)
        input_coords = carray(input_ptr, (output_rank,), dtype=float64)
        jitted_function(output_coords, input_coords)
        return 1
    return LowLevelCallable(wrapped.ctypes)
