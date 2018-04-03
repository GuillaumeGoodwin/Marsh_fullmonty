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
get_MOA = False ; plot_MOA = True


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

#BTP2 failed
#CRO2 failed
#FLX1 failed

# Test the plots on BTP1, CRO3, FLX2, HIN1,
Sites = ["BTP1", "CRO3", "FLX2", "HIN1"]
# ... change the extent to something smaller.

#MSY is looooong. Skip it for now
#SFT2 is looooong. Skip it for now
#MCB IS sooooo looong. I might skip it....

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
    if plot_MOA is True:
        # Run the TIP marsh finder
        os.system("cd " +  MOA_dir + " && python MarshOutlineAnalysis.py -dir " + DEM_dir+site+"/" + " -site " + site + " -Plot " + str(plot_MOA))
        #os.system("cd " +  MOA_dir + " && python MarshOutlineAnalysis.py -dir " + DEM_dir+site+"/" + " -site " + site + " -MOA "+ str(get_MOA) + "-Plot" + str(plot_MOA))

        quit()
