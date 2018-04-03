"""Introductory chat"""


import os
import sys



def write_LSD_Driver (dr_path, dr_name, r_path, w_path, r_fname, w_fname):

    outf = open(dr_path+dr_name+'.driver', 'w')

    outf.write("read path: " + r_path + '\n')
    outf.write("write path: " + w_path + '\n')
    outf.write("read fname: " + r_fname + '\n')
    outf.write("write fname: " + w_fname + '\n')
    outf.write("channel heads fname: NULL" + '\n')
    outf.write("remove_seas: false" + '\n')
    outf.write("write_hillshade: true" + '\n')
    outf.write("surface_fitting_radius: 1" + '\n')
    outf.write("print_slope: true" + '\n')
    outf.write("print_curvature: true" + '\n')
    outf.write("print_wiener_filtered_raster: false" + '\n')

    outf.close()
