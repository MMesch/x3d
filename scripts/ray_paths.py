#!/usr/bin/env python

from obspy import read_inventory, read_events
from obspy.imaging.ray_paths import plot_rays

def test_path_plotting():
    data_path = 'IU_stations.txt'
    inventory = read_inventory(data_path)
    catalog = read_events()

    # this test uses the resampling method along the CMB
    plot_rays(inventory=inventory, catalog=catalog,
              phase_list=['Pdiff'], colorscheme='dark',
              kind='mayavi', icol=2, fname_out='scene.x3d')

if __name__ == '__main__':
    test_path_plotting()
