"""
Batch_Metrics_TIP_MOA.py

This script runs the complete package necessary to get a MOA:
A. Prepares your inputs by:
    1. Converting the DEM to the ENVI format used by LSDTopoTools
    2. Applying a Wiener filter (optional)
    3. Calculating basic topographic metrics (slope, curvature and hillshade)
    5. Clipping these inputs to a specified domain

B. Performs the TIP marsh detection
    1.

C. Performs the MOA
    1.

NB: This file is extremely sensitive to directory structure, so make sure you set it up correctly.
NB2: This file can sit anywhere. It uses only absolute paths.
"""

import os
import sys

from Batch_functions import *


################################################################################
#=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-#
################################################################################
# Step 1: Select the actions to perform
get_metrics = False ; Filter = False
get_TIP = False ; plot_TIP = False
get_MOA = True ; plot_MOA = False


################################################################################
#=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-#
################################################################################
# Step 2: Set up the directory structure. Do it. Really. It's important.
data_dir = "/home/willgoodwin/Data/"
DEM_dir = data_dir + "EA_LiDAR/"
Driver_dir = data_dir + "Driver/"
Domain_dir = data_dir + "Domain/"

LSD_dir = "/home/willgoodwin/Software/LSDTopoTools/"
Wiener_dir = LSD_dir + "LSD_Analysis_Driver/"
Metrics_dir = LSD_dir + "LSD_Analysis_Driver/LSDTopoTools_AnalysisDriver/Analysis_driver/"
TIP_dir = LSD_dir + "LSDCoastal/LSD_TIP/LSDTopoTools_MarshPlatform/"
MOA_dir = LSD_dir + "LSDCoastal/LSD_MOA"


# Also set the names you want to give to your files
DEM_suffix = "_DEM"
Slope_suffix = "_Slope"
Curv_suffix = "_Curv"
Wiener_suffix = "_W_"



################################################################################
#=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-#
################################################################################
# Step 3: Choose the study sites and the CRS
Sites = ["CRO1", "CRO2","CRO3","FLX1","FLX2","PGL","RYE", "SFT1","SFT2","SWA1","SWA2","SWA3","WSH1","WSH2","WSH3","WSH4"]
#Sites left:
#Sites = ["CTC", "EXM","LYM1","LYM2","POO1","PO02","PGM", "SOL"]
#Problems here!
#Sites = ["BTP2"]
#Sites done= ["BTP1", "HIN1", "HIN2", "WST1", "WST2", "SVN", "BTP1", "BTP1", "BTP1", ]
# MSY TIP OK - big site
# MCB TIP OK - big site
# CRO3 TIP not finished
# CTC not great. Better leave it out.
# EXM Marshes almost invisible. Let's give it a go anyway.
# PGL not great because accreting



# That's it, I'm adding US sites.
#WOO (Cape Cod)
# And French Sites.

# Redo WSH1, WSH2

# Good sistes for TIP - Proceed to MOA
#BTP1
#BTP2
#CRO2
#CRO3
#FLX1
#FLX2
#HIN1
#MSY
#SFT2
#MCB
#SWA1
#SWA3
#LYM1
#LYM2
#POO1
#POO2
#POO3
#SOL
#WSH4

Sites = ["BTP1",
"BTP2",
"CRO2",
"CRO3",
"FLX1",
"FLX2",
"HIN1",
"MSY",
"SFT2",
"MCB",
"SWA1",
"SWA3",
"LYM1",
"LYM2",
"POO1",
"POO2",
"POO3",
"SOL",
"WSH4"]


"""Sites = [
"MCB",
"SWA1",
"SWA3","""

Sites = [
"LYM1",
"LYM2",
"POO1",
"POO2",
"POO3",
"SOL",
"WSH4"]

#BTP2 failed
#CRO2 failed
#FLX1 failed


#improve the system by tiling and deleting stuff from the list of segments

# Test the plots on BTP1, CRO3, FLX2, HIN1,

# ... change the extent to something smaller for most sites.

#MSY is looooong. Skip it for now
#SFT2 is looooong. Skip it for now
#MCB IS sooooo looong. I might skip it and change the domain
# Same for SWA1


# Next up: Make sure each site has a wave + TR file.

# Get wind data and fetch (somehow) for ech site/direction
# Find a way to represent the direction of transect vs direction of waves
# Think about the poster and its message!!!!!!





CRS = "EPSG:27700"
Nodata_value = -9999

################################################################################
#=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-#
################################################################################
# Now we can run the batch script
for site in Sites:
    if get_metrics is True:
        # Put the DEM in the rigth format
        src_dir = DEM_dir + site + "/"
        dst_dir = DEM_dir + site + "/"
        src = src_dir + site + ".tiff"
        dst = src_dir + site + ".bil"
        os.system("gdal_translate -of ENVI -a_srs "+ CRS + " " + src + " " +  dst)

        if Filter is True:
            # Make a filtered DEM
            src = dst
            dst = DEM_dir + site + "/" + site + Wiener_suffix + ".bil"
            os.system("./Wiener_filter.out " + sourcedir + sourcefile +  sourceformat)

        # Calculate the metrics
        write_LSD_Driver (Driver_dir, site, DEM_dir+site+"/", DEM_dir+"/"+site+"/", site, site)
        src = dst
        driver = site + ".driver"
        os.system("cd " +  Metrics_dir + " && ./LSDTT_BasicMetrics.out " + Driver_dir + " " + driver)

        # Clip inputs to the domain
        input_data = ["", "_SLOPE", "_CURV","_hs"]
        clipped_data = ["_DEM_clip", "_SLOPE_clip", "_CURV_clip","_hs_clip"]
        domain = Domain_dir + site + "_domain.shp"
        for i in range(len(input_data)):
            src = DEM_dir + site + "/" + site + input_data[i]+".bil"
            dst = DEM_dir + site + "/" + site + clipped_data[i]+".bil"
            os.system("gdalwarp -overwrite -of ENVI -t_srs " + CRS + " -cutline " + domain + " -crop_to_cutline " + src + " " + dst)

    if get_TIP is True:
        # Run the TIP marsh finder
        os.system("cd " +  TIP_dir + " && python MarshPlatformAnalysis.py -dir " + DEM_dir+site+"/" + " -site " + site + " -MID "+ str(get_TIP) + "-MIDP" + str(plot_TIP))

    if get_MOA is True:
        # Run the TIP marsh finder
        os.system("cd " +  MOA_dir + " && python MarshOutlineAnalysis.py -dir " + DEM_dir+site+"/" + " -site " + site + " -MOA "+ str(get_MOA) + "-Plot" + str(plot_MOA))
        #os.system("cd " +  MOA_dir + " && python MarshOutlineAnalysis.py -dir " + DEM_dir+site+"/" + " -site " + site + " -MOA "+ str(get_MOA) + "-Plot" + str(plot_MOA))
