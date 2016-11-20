#!/usr/bin/env python

from obspy.imaging.source import plot_radiation_pattern
import numpy as np


def main():
    # mt = [1., 1., 1., 0., 0., 0.]  # explosion
    # mt = [0., 0., 0., 1., -1., 0.]  # double couple
    mt = [0., 0., 0., 1., -1., -1.]
    plot_radiation_pattern(mt, kind='mayavi')

if __name__ == "__main__":
    main()
