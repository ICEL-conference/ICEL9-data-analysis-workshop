from __future__ import annotations

import numpy as np
from scipy import interpolate as interp
from enum import Enum
import copy

class InterpolationEnum(Enum):
    nearest = 0, interp.interp1d, dict(kind="nearest", fill_value="extrapolate")
    pchip = 1, interp.PchipInterpolator, dict(extrapolate=True)
    spline = 2, interp.InterpolatedUnivariateSpline, dict(k=3, ext=0)

    def __new__(cls, *args, **kwargs):
        obj = object.__new__(cls)
        obj._value_ = args[0]
        return obj

    def __init__(self, _: int, interpolation_class = None, kwargs = None):
        self._interpolation_class = interpolation_class
        self._kwargs = kwargs

    def fill_missing(self, data: np.ndarray, max_gap_length ,**kwargs):

        # Make sure the input kwargs exist in enum define kwargs
        new_kwargs = copy.copy(self._kwargs)
        for key in kwargs:
            if key in new_kwargs:
                new_kwargs[key] = kwargs[key]
        return fill_missing(data=data, interpolator=self._interpolation_class, max_gap_length=max_gap_length,  **new_kwargs)


def fill_missing(data: np.ndarray, interpolator, max_gap_length,  **kwargs) -> np.ndarray:

    # Create indices array
    indices = np.arange(data.shape[0])

    # Get the finite indices as bools
    finite = np.isfinite(data) if data.ndim == 1 else np.isfinite(data[:, 0])

    # Create interpolation object
    f = interpolator(indices[finite], data[finite], **kwargs)

    # Get interpolated new data
    filled_data = np.where(np.isfinite(data), data, f(indices))

    # Get only the previously filled
    only_filled = np.where(np.isnan(data), f(indices), np.nan)

    # put back nan where gaps are longer than max gap length
    st, en, le = nan_start_stop(data=data)
    for segment_cnt, segment_len in enumerate(le):
        if segment_len > max_gap_length:
            filled_data[st[segment_cnt]: en[segment_cnt]] = np.nan
            only_filled[st[segment_cnt]: en[segment_cnt]] = np.nan

    return filled_data, only_filled


def nan_start_stop(data: np.ndarray):
    # Squeeze
    data = np.squeeze(data)

    # Create indexes
    N = data.size
    inds = np.arange(N)

    # Create vector where nans are zeros and finite numbers are ones
    x = np.zeros(N)
    x[np.isfinite(data)] = 1

    # Prepend a 1 and differentiate
    x = np.hstack((1, x))
    xd = np.diff(x)

    # Start index and stop index depending on edge
    start = inds[xd < 0]
    stop = inds[xd > 0]

    # if start and stop are not the same length append last frame to stop
    if start.shape != stop.shape:
        stop = np.hstack((stop, N - 1))

    # Calculate length of nan segments
    length = stop - start

    return start, stop, length
